"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.MultiLabelSoftMarginLoss\ntorch.nn.MultiLabelSoftMarginLoss(weight=None, size_average=None, reduce=None, reduction='mean')\n"
import torch
import torch.nn as nn
input = torch.tensor([[0.1, 0.2, 0.9], [0.1, 0.2, 0.3], [0.1, 0.2, 0.3]], requires_grad=True)
target = torch.tensor([[1, 0, 1], [0, 0, 1], [0, 1, 0]])
loss_fn = nn.MultiLabelSoftMarginLoss()
loss = loss_fn(input, target)
print(loss)