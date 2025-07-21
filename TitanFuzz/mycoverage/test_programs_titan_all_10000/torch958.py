import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(1, 1, 4, requires_grad=True)
output = torch.nn.functional.adaptive_avg_pool1d(input, 1)