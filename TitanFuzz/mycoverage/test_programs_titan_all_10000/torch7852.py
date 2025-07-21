import torch
from torch import nn
from torch.autograd import Variable
input = torch.tensor([[True, False], [False, False], [True, True]])
other = torch.tensor([[False, True], [False, False], [True, True]])
torch.logical_xor(input, other)
input = torch.tensor([[True, False], [False, False], [True, True]])
torch.logical_not(input)