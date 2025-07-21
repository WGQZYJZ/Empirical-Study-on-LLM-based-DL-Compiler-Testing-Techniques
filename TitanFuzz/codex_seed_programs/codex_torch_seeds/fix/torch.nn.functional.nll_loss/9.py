"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.nll_loss\ntorch.nn.functional.nll_loss(input, target, weight=None, size_average=None, ignore_index=-100, reduce=None, reduction='mean')\n"
import torch
import torch.nn as nn
import torch.nn.functional as F
input_data = torch.randn(3, 5, requires_grad=True)
target = torch.empty(3, dtype=torch.long).random_(5)
loss = F.nll_loss(input_data, target)
print(loss)
loss = F.nll_loss(input_data, target, reduction='sum')
print(loss)
loss = F.nll_loss(input_data, target, reduction='none')
print(loss)