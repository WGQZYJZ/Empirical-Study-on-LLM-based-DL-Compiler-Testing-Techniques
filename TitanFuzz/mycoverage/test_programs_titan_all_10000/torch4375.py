import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(3, 5, requires_grad=True)
target = torch.empty(3, dtype=torch.long).random_(5)
loss = torch.nn.MultiMarginLoss()
output = loss(input, target)
input = torch.randn(3, 5, requires_grad=True)
target = torch.empty(3, dtype=torch.long).random_(5)
loss = torch.nn.MultiMarginLoss(p=2, margin=1.0, weight=None, size_average=None, reduce=None, reduction='mean')
output = loss(input, target)