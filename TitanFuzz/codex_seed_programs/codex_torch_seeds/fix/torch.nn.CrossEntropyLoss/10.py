"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.CrossEntropyLoss\ntorch.nn.CrossEntropyLoss(weight=None, size_average=None, ignore_index=-100, reduce=None, reduction='mean')\n"
import torch
import torch.nn as nn
import torch.nn.functional as F
(N, C) = (4, 5)
input = torch.randn(N, C, requires_grad=True)
target = torch.empty(N, dtype=torch.long).random_(C)
loss = nn.CrossEntropyLoss()
output = loss(input, target)
print(output)
input = torch.randn(N, C, requires_grad=True)
target = torch.empty(N, dtype=torch.long).random_(C)
output = F.cross_entropy(input, target)
print(output)