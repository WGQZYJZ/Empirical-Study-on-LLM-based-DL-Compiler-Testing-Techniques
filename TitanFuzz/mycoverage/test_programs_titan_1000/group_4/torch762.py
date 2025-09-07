import torch
from torch import nn
from torch.autograd import Variable
input = torch.rand(4, 3)
vec = torch.rand(3)
output = torch.mv(input, vec)