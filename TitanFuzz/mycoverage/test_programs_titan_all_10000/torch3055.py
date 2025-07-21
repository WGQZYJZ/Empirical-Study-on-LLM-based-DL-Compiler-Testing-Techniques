import torch
from torch import nn
from torch.autograd import Variable
input = torch.rand(3, 5)
vec = torch.rand(5)
output = torch.mv(input, vec)