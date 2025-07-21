import torch
from torch import nn
from torch.autograd import Variable
x = torch.tensor([[True, True], [True, False], [False, True], [False, False]])
y = torch.tensor([[True, False], [True, True], [False, False], [False, True]])
z = torch.logical_xor(x, y)