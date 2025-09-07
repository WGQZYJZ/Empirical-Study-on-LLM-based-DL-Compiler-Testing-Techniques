import torch
from torch import nn
from torch.autograd import Variable
input = torch.tensor([[1, 2, 3], [4, 5, 6]])
other = torch.tensor([[7, 8], [9, 10], [11, 12]])
res = torch.kron(input, other)