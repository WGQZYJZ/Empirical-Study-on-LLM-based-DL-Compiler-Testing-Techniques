import torch
from torch import nn
from torch.autograd import Variable
input = Variable(torch.randn(1, 1, 4))
pool = torch.nn.LPPool1d(norm_type=2, kernel_size=2, stride=2)
output = pool(input)