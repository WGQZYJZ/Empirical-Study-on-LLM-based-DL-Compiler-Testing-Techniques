import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(3, 5)
vec = torch.randn(5)
output = torch.mv(input, vec)