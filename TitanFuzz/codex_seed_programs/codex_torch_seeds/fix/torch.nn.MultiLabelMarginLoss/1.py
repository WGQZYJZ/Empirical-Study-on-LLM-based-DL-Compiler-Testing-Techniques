"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.MultiLabelMarginLoss\ntorch.nn.MultiLabelMarginLoss(size_average=None, reduce=None, reduction='mean')\n"
import torch
import torch.nn as nn
x = torch.rand(3, 4)
y = torch.tensor([[0, 1, 0, 1], [1, 0, 1, 0], [1, 1, 1, 0]])
loss = nn.MultiLabelMarginLoss()
print(loss(x, y))