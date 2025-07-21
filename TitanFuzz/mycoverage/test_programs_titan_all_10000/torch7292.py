import torch
from torch import nn
from torch.autograd import Variable
input = torch.tensor([[True, False], [False, False]], dtype=torch.bool)
other = torch.tensor([[False, False], [False, True]], dtype=torch.bool)
output = torch.logical_or(input, other)