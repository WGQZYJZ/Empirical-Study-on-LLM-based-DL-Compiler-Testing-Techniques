"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.MultiLabelSoftMarginLoss\ntorch.nn.MultiLabelSoftMarginLoss(weight=None, size_average=None, reduce=None, reduction='mean')\n"
import torch
import torch.nn as nn
input = torch.randn(3, requires_grad=True)
target = torch.empty(3).random_(2)
loss = nn.MultiLabelSoftMarginLoss()
output = loss(input, target)
print(output)