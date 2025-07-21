import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(4, 4)
output = torch.full_like(input, fill_value=2.0)