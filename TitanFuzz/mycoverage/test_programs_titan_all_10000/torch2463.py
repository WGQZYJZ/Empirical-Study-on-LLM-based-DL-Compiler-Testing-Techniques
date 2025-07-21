import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(1, 2, 5)
output = torch.nn.functional.adaptive_avg_pool1d(input, 2)