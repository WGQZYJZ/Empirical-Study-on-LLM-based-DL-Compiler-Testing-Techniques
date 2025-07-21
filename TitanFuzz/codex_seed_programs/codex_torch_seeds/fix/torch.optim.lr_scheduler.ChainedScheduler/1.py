'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.optim.lr_scheduler.ChainedScheduler\ntorch.optim.lr_scheduler.ChainedScheduler(schedulers)\n'
import torch
import torch.nn as nn
import torch.optim as optim
import torch.nn.functional as F
import torch.optim.lr_scheduler as lr_scheduler
x = torch.randn(100, 10)
y = torch.randint(0, 10, (100,))
model = nn.Linear(10, 1)
optimizer = optim.SGD(model.parameters(), lr=0.001)
scheduler1 = lr_scheduler.StepLR(optimizer, step_size=10, gamma=0.1)
scheduler2 = lr_scheduler.ExponentialLR(optimizer, gamma=0.5)
scheduler = lr_scheduler.ChainedScheduler([scheduler1, scheduler2])