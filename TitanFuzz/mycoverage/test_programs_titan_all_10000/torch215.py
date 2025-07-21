import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(1, 5)
output = torch.acos(input)