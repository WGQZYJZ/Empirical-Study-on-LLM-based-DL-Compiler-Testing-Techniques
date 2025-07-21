"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.SmoothL1Loss\ntorch.nn.SmoothL1Loss(size_average=None, reduce=None, reduction='mean', beta=1.0)\n"
import torch
from torch.autograd import Variable
x = Variable(torch.randn(1, 1, 3, 3))
y = Variable(torch.randn(1, 1, 3, 3))
loss = torch.nn.SmoothL1Loss()
print(loss(x, y))