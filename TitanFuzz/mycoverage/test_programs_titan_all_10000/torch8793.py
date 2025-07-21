import torch
from torch import nn
from torch.autograd import Variable
input = torch.tensor([[1, 2], [3, 4]])
other = torch.tensor([[5, 6], [7, 8]])
torch.kron(input, other)
input = torch.randn(4)
torch.log(input)
input = torch.randn(4)
torch.log10(input)