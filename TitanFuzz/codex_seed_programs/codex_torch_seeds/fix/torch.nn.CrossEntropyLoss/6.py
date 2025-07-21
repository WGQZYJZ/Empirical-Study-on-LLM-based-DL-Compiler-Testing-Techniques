"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.CrossEntropyLoss\ntorch.nn.CrossEntropyLoss(weight=None, size_average=None, ignore_index=-100, reduce=None, reduction='mean')\n"
import torch
import torch.nn as nn
(N, C) = (5, 4)
x = torch.randn(N, C, requires_grad=True)
target = torch.empty(N, dtype=torch.long).random_(C)
print(x)
print(target)
loss = nn.CrossEntropyLoss()
output = loss(x, target)
print(output)
output.backward()
print(x.grad)
weight = torch.tensor([1.0, 2.0, 3.0, 4.0], dtype=torch.float)
loss = nn.CrossEntropyLoss(weight=weight)
output = loss(x, target)
print(output)
output.backward()
print(x.grad)