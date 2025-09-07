import torch
from torch import nn
from torch.autograd import Variable

input = torch.randn(5, 3, dtype=torch.float)
output = torch.randn_like(input)