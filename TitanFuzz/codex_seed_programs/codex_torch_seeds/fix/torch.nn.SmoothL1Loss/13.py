"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.SmoothL1Loss\ntorch.nn.SmoothL1Loss(size_average=None, reduce=None, reduction='mean', beta=1.0)\n"
import torch
from torch.autograd import Variable
import numpy as np
x = Variable(torch.randn(2, 3), requires_grad=True)
y = Variable(torch.randn(2, 3), requires_grad=True)
loss = torch.nn.SmoothL1Loss()
print(loss(x, y))
print(x.grad)
print(y.grad)