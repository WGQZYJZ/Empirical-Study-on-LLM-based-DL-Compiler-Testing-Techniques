import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(2, 3)
other = torch.randn(3, 4)
out = torch.linalg.matmul(input, other)
out = torch.matmul(input, other)