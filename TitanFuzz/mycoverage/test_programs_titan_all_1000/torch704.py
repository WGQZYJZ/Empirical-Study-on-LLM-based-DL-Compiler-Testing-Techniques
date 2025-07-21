import torch
from torch import nn
from torch.autograd import Variable
input = torch.tensor([[True, False], [True, True]], dtype=torch.bool)
other = torch.tensor([[True, True], [False, True]], dtype=torch.bool)
torch.logical_and(input, other)