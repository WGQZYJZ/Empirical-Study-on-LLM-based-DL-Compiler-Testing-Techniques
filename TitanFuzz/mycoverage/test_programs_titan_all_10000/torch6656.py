import torch
from torch import nn
from torch.autograd import Variable
input = Variable(torch.Tensor(1, 1, 3, 3, 3))
input = input.fill_(2)
input[(0, 0, 1, 1, 1)] = 8
pool = torch.nn.AvgPool3d(kernel_size=3, stride=1, padding=0)
output = pool(input)