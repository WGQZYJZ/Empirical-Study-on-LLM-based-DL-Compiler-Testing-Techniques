import torch
from torch import nn
from torch.autograd import Variable
input = Variable(torch.randn(1, 1, 5, 5, 5))
max_pool3d = torch.nn.functional.max_pool3d(input, kernel_size=3, stride=1, padding=1)