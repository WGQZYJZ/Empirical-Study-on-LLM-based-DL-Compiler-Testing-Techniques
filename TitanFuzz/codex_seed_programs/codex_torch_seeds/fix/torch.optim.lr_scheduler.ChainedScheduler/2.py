'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.optim.lr_scheduler.ChainedScheduler\ntorch.optim.lr_scheduler.ChainedScheduler(schedulers)\n'
import torch
import torch.nn as nn
import torch.optim as optim
import torch.optim.lr_scheduler as lr_scheduler
input = torch.randn(1, 1, requires_grad=True)
target = torch.randn(1, 1)
model = nn.Linear(1, 1)
optimizer = optim.SGD(model.parameters(), lr=0.1)
scheduler = lr_scheduler.ChainedScheduler([lr_scheduler.StepLR(optimizer, step_size=3, gamma=0.1), lr_scheduler.StepLR(optimizer, step_size=5, gamma=0.1), lr_scheduler.StepLR(optimizer, step_size=7, gamma=0.1)])
for i in range(10):
    optimizer.zero_grad()
    output = model(input)