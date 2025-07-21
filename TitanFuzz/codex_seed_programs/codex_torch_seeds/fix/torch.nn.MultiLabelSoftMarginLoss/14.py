"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.MultiLabelSoftMarginLoss\ntorch.nn.MultiLabelSoftMarginLoss(weight=None, size_average=None, reduce=None, reduction='mean')\n"
import torch
import torch.nn as nn
import torch.nn.functional as F
input = torch.randn(3, 5, requires_grad=True)
target = torch.empty(3, 5).random_(2)
print('Task 1: import PyTorch')
print('PyTorch version: ', torch.__version__)
print('\nTask 2: Generate input data')
print('Input data: ', input)
print('Target data: ', target)
print('\nTask 3: Call the API torch.nn.MultiLabelSoftMarginLoss')
loss = nn.MultiLabelSoftMarginLoss()
output = loss(input, target)
print('Loss: ', output)