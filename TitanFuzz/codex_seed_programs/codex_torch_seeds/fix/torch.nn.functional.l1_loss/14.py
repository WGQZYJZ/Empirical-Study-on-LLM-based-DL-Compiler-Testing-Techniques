"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.l1_loss\ntorch.nn.functional.l1_loss(input, target, size_average=None, reduce=None, reduction='mean')\n"
import torch
import torch.nn.functional as F
input = torch.randn(3, 5, requires_grad=True)
target = torch.randn(3, 5)
loss = F.l1_loss(input, target)
print(loss)
"\nTask 4: Call the API torch.nn.L1Loss\ntorch.nn.L1Loss(size_average=None, reduce=None, reduction='mean')\n"
import torch
import torch.nn as nn
mse_loss = nn.L1Loss()
input = torch.randn(3, 5, requires_grad=True)
target = torch.randn(3, 5)
loss = mse_loss(input, target)
print(loss)