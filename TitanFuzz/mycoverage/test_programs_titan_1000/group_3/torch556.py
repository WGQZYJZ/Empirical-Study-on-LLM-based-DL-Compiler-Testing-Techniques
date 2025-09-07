import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(1, 16, 10, 10, 10)
output = torch.nn.functional.adaptive_max_pool3d(input, (5, 5, 5))