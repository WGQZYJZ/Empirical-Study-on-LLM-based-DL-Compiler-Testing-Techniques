import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(1, 3)
result = torch.aminmax(input, dim=1)