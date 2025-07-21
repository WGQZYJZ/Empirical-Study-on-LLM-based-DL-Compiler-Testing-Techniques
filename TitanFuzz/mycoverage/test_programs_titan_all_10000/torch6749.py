import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(1, 1, 4)
output = torch.nn.functional.avg_pool1d(input, 2, stride=2)