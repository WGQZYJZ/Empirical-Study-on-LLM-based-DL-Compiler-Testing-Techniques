"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.SmoothL1Loss\ntorch.nn.SmoothL1Loss(size_average=None, reduce=None, reduction='mean', beta=1.0)\n"
import torch
import torch.nn as nn
x = torch.tensor([[1, 2, 3], [4, 5, 6]], dtype=torch.float)
y = torch.tensor([[1, 2, 3], [4, 5, 6]], dtype=torch.float)
loss = nn.SmoothL1Loss()
print(loss(x, y))