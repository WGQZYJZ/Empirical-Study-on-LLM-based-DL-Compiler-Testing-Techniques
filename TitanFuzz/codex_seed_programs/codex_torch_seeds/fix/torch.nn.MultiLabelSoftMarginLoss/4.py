"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.MultiLabelSoftMarginLoss\ntorch.nn.MultiLabelSoftMarginLoss(weight=None, size_average=None, reduce=None, reduction='mean')\n"
import torch
import torch.nn as nn
input = torch.tensor([[1.0, (- 1.0), 1.0], [1.0, 1.0, (- 1.0)]], requires_grad=True)
target = torch.tensor([[0.0, 1.0, 1.0], [1.0, 0.0, 1.0]])
loss = nn.MultiLabelSoftMarginLoss()
output = loss(input, target)
print(output)