import torch
from torch import nn
from torch.autograd import Variable
input = torch.tensor([[True, False], [True, True], [False, False], [False, True]])
other = torch.tensor([[True, True], [True, True], [False, False], [False, True]])
torch.logical_xor(input, other, out=None)