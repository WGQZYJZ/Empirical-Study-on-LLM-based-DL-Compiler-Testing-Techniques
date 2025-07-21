import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(2, 3)
vec = torch.randn(3)
torch.mv(input, vec)