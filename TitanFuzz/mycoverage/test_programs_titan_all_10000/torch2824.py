import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(1, 1, 64, 64, 64)
output = torch.nn.functional.adaptive_max_pool3d(input, (1, 1, 1))