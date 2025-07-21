"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.smooth_l1_loss\ntorch.nn.functional.smooth_l1_loss(input, target, size_average=None, reduce=None, reduction='mean', beta=1.0)\n"
import torch
from torch.autograd import Variable
import numpy as np
import torch
from torch.autograd import Variable
x = Variable(torch.randn(1, 1, 3, 3))
print('x:', x)
print('x.size():', x.size())
y = Variable(torch.Tensor([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0], [7.0, 8.0, 9.0]]))
print('y:', y)
print('y.size():', y.size())
loss = torch.nn.functional.smooth_l1_loss(x, y)
print('loss:', loss)