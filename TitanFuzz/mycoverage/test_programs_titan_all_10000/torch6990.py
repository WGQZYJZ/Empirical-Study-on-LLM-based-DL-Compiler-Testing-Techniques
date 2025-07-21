import torch
from torch import nn
from torch.autograd import Variable
input = Variable(torch.randn(1, 1, 4))
output = torch.nn.functional.max_pool1d(input, kernel_size=2, stride=1, padding=0)