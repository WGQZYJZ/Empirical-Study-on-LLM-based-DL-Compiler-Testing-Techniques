import torch
from torch import nn
from torch.autograd import Variable
input = Variable(torch.randn(1, 1, 4, 4))
pool = torch.nn.MaxPool2d(2, stride=2, return_indices=True)
unpool = torch.nn.MaxUnpool2d(2, stride=2)
(output, indices) = pool(input)
unpool(output, indices)