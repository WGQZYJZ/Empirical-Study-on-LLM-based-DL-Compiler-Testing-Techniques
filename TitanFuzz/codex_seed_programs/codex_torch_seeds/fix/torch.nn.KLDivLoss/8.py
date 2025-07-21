"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.KLDivLoss\ntorch.nn.KLDivLoss(size_average=None, reduce=None, reduction='mean', log_target=False)\n"
import torch
import torch.nn as nn
import numpy as np
input = torch.Tensor([[0.1, 0.2, 0.3, 0.4], [0.1, 0.2, 0.3, 0.4]])
target = torch.Tensor([[0.05, 0.1, 0.15, 0.7], [0.05, 0.1, 0.15, 0.7]])
loss = nn.KLDivLoss(size_average=False, reduce=False)
output = loss(input, target)
print(output)
loss = nn.KLDivLoss(size_average=True, reduce=False)
output = loss(input, target)
print(output)