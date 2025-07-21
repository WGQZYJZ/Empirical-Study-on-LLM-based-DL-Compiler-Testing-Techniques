"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.optim.lr_scheduler.ReduceLROnPlateau\ntorch.optim.lr_scheduler.ReduceLROnPlateau(optimizer, mode='min', factor=0.1, patience=10, threshold=0.0001, threshold_mode='rel', cooldown=0, min_lr=0, eps=1e-08, verbose=False)\n"
import torch
import torch.nn as nn
import torch.optim as optim
import torch.nn.functional as F
from torch.optim.lr_scheduler import ReduceLROnPlateau
x = torch.randn(1, requires_grad=True)
y = torch.randn(1, requires_grad=True)
optimizer = optim.SGD([x, y], lr=0.001)
scheduler = ReduceLROnPlateau(optimizer, 'min')
for i in range(100):
    optimizer.zero_grad()
    loss = ((x ** 2) + (y ** 2))
    loss.backward()
    optimizer.step()
    scheduler.step(loss)
    print('x:', x.item(), 'y:', y.item(), 'loss:', loss.item())