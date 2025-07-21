"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.BCEWithLogitsLoss\ntorch.nn.BCEWithLogitsLoss(weight=None, size_average=None, reduce=None, reduction='mean', pos_weight=None)\n"
import torch
from torch.autograd import Variable
import torch.nn as nn
import torch
from torch.autograd import Variable
import torch.nn as nn
input = Variable(torch.randn(3, 5), requires_grad=True)
target = Variable(torch.randn(3, 5))
loss = nn.BCEWithLogitsLoss()
output = loss(input, target)
output.backward()
print('input:', input)
print('target:', target)
print('output:', output)
print('input.grad:', input.grad)
print('target.grad:', target.grad)
print('output.grad:', output.grad)