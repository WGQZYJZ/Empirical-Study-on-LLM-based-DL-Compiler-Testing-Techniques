"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.SoftMarginLoss\ntorch.nn.SoftMarginLoss(size_average=None, reduce=None, reduction='mean')\n"
import torch
import torch.nn as nn
from torch.autograd import Variable
input = Variable(torch.randn(3, 5), requires_grad=True)
target = Variable(torch.randn(3, 5))
loss = nn.SoftMarginLoss()
output = loss(input, target)
print(output)
print(output.item())