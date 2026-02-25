def train_epoch(model, dataloader, optimizer, criterion, device):
    model.train()
    running_loss = 0.0
    correct = 0
    total = 0
    train_preds, train_targets = [], []
    for batch in train_loader:
        optimizer.zero_grad()
        out = model(batch.x.to(device), batch.edge_index.to(device))
        loss = criterion(out, batch.y.to(device))
        loss.backward()
        optimizer.step()
        
        running_loss += loss.item()
        _, predicted = torch.max(outputs.data, 1)
        val_preds.extend(predicted.cpu().numpy())
        val_targets.extend(batch.y.cpu().numpy())
    
    epoch_loss = running_loss / len(dataloader)
    epoch_f1 = f1_score(train_targets, train_preds, average='macro')
    
    return epoch_loss, epoch_f1

def validate(model, dataloader, criterion, device):
    model.eval()
    running_loss = 0.0
    correct = 0
    total = 0
    val_preds, val_targets = [], []
    with torch.no_grad():
        for batch in val_loader:
            out = model(batch.x.to(device), batch.edge_index.to(device))
            loss = criterion(out, batch.y.to(device))
            preds = out.argmax(dim=-1)
            val_preds.extend(preds.cpu().numpy())
            val_targets.extend(batch.y.cpu().numpy())
            running_loss += loss.item()
            
    val_f1 = f1_score(val_targets, val_preds, average='macro')
    val_loss = running_loss / len(dataloader)
    
    return val_loss, val_f1
    
    
def train_model(
    model,
    train_loader,
    val_loader,
    optimizer,
    scheduler,
    criterion,
    device,
    epochs=20,
    use_wandb=True,
    wandb_name='new project'
):
    if use_wandb:
        wandb.init(project=wandb_name)
        wandb.watch(model)
    
    best_val_f1 = 0.0
    history = {
        'train_loss': [],
        'train_f1': [],
        'val_loss': [],
        'val_f1': [],
        'lr': []
    }
    
    for epoch in range(epochs):
        train_loss, train_f1 = train_epoch(
            model, train_loader, optimizer, criterion, device
        )
        val_loss, val_f1 = validate(
            model, val_loader, criterion, device
        )
        
        # Обновление scheduler
        if isinstance(scheduler, lr_scheduler.ReduceLROnPlateau):
            scheduler.step(val_f1)
        else:
            scheduler.step()
        
        current_lr = optimizer.param_groups[0]['lr']
        
        # Логирование
        history['train_loss'].append(train_loss)
        history['train_f1'].append(train_f1)
        history['val_loss'].append(val_loss)
        history['val_f1'].append(val_f1)
        history['lr'].append(current_lr)
        
        print(f"Epoch {epoch+1}/{epochs}:")
        print(f"  Train Loss: {train_loss:.4f} | F1: {train_f1:.4f}")
        print(f"  Val Loss: {val_loss:.4f} | F1: {val_f1:.4f}")
        print(f"  LR: {current_lr:.6f}")
        
        if use_wandb:
            wandb.log({
                "epoch": epoch,
                "train_loss": train_loss,
                "train_f1": train_f1,
                "val_loss": val_loss,
                "val_f1": val_f1,
                "lr": current_lr
            })
        
        # Сохранение лучшей модели
        if val_f1 > best_val_f1:
            best_val_f1 = val_f1
            torch.save(model.state_dict(), 'best_model.pth')
    
    if use_wandb:
        wandb.finish()
    
    return history

import matplotlib.pyplot as plt

def plot_training_history(history):
    plt.figure(figsize=(12, 4))
    
    # Loss
    plt.subplot(1, 2, 1)
    plt.plot(history['train_loss'], label='Train')
    plt.plot(history['val_loss'], label='Validation')
    plt.title('Loss')
    plt.xlabel('Epoch')
    plt.legend()
    
    # Accuracy
    plt.subplot(1, 2, 2)
    plt.plot(history['train_f1'], label='Train')
    plt.plot(history['val_f1'], label='Validation')
    plt.title('F1-score')
    plt.xlabel('Epoch')
    plt.legend()
    
    plt.tight_layout()
    plt.show()

    # Learning rate
    plt.figure(figsize=(6, 4))
    plt.plot(history['lr'])
    plt.title('Learning Rate Schedule')
    plt.xlabel('Epoch')
    plt.ylabel('LR')
    plt.show()
