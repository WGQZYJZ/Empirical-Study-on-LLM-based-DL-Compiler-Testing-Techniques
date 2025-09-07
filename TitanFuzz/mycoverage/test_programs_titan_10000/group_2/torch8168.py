import torch
from torch import nn
from torch.autograd import Variable

x = torch.tensor([[True, False], [True, True]])
y = torch.tensor([[False, False], [True, False]])
z = torch.logical_or(x, y)
x = torch.tensor([[True, False], [True, True]])
y = torch.tensor([[False, False], [True, False]])
z = torch.logical_and(x, y)
x = torch.tensor([[True, False], [True, True]])
y = torch.tensor([[False, False], [True, False]])
z = torch.logical_xor(x, y)