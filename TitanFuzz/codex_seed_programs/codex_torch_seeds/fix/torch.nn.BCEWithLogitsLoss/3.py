"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.BCEWithLogitsLoss\ntorch.nn.BCEWithLogitsLoss(weight=None, size_average=None, reduce=None, reduction='mean', pos_weight=None)\n"
import torch
import torch.nn as nn
import torch
import torch.nn as nn
input = torch.randn(3, requires_grad=True)
target = torch.empty(3).random_(2)
loss = nn.BCEWithLogitsLoss()
output = loss(input, target)
print(output)
output.backward()
print(input.grad)
loss = nn.BCEWithLogitsLoss(reduction='sum')
output = loss(input, target)
print(output)
loss = nn.BCEWithLogitsLoss(reduction='none')
output = loss(input, target)
print(output)