"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.CrossEntropyLoss\ntorch.nn.CrossEntropyLoss(weight=None, size_average=None, ignore_index=-100, reduce=None, reduction='mean')\n"
import torch
import torch.nn as nn
x = torch.randn(3, 5, requires_grad=True)
y = torch.tensor([1, 0, 4])
criterion = nn.CrossEntropyLoss()
loss = criterion(x, y)
print(loss)