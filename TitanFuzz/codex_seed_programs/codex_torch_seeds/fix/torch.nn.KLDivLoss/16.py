"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.KLDivLoss\ntorch.nn.KLDivLoss(size_average=None, reduce=None, reduction='mean', log_target=False)\n"
import torch
import torch.nn as nn
input = torch.tensor([[1, 2, 3, 4], [2, 3, 4, 5]])
target = torch.tensor([[1, 2, 3, 4], [2, 3, 4, 5]])
loss = nn.KLDivLoss()
output = loss(input, target)
print(output)