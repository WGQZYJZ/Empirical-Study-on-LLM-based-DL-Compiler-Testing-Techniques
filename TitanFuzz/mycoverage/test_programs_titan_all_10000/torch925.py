import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(3, 4, 5)
output = torch.rot90(input, k=1, dims=(1, 2))
input = torch.randn(3, 4, 5)
output = torch.rot90(input, k=2, dims=(1, 2))