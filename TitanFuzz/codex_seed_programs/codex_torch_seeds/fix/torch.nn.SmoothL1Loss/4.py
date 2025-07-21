"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.SmoothL1Loss\ntorch.nn.SmoothL1Loss(size_average=None, reduce=None, reduction='mean', beta=1.0)\n"
import torch
import torch.nn as nn
input = torch.randn(3, 5, requires_grad=True)
target = torch.randn(3, 5)
loss = nn.SmoothL1Loss()
output = loss(input, target)
print(output)
"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.MSELoss\ntorch.nn.MSELoss(size_average=None, reduce=None, reduction='mean')\n"
import torch
import torch.nn as nn
input = torch.randn(3, 5, requires_grad=True)
target = torch.randn(3, 5)
loss = nn.MSELoss()
output = loss(input, target)
print(output)