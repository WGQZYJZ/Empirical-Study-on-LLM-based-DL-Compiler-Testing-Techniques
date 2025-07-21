import torch
from torch import nn
from torch.autograd import Variable
input = Variable(torch.randn(1, 1, 3, 3, 3))
output = torch.nn.functional.max_pool3d(input, kernel_size=3, stride=2, padding=0)