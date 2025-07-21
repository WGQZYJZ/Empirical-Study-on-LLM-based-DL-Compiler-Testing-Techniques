import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(4, 5)
result = torch.std(input)