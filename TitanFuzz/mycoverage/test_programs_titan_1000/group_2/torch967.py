import torch
from torch import nn
from torch.autograd import Variable
input = torch.tensor([[True, False], [False, True]])
output = torch.logical_not(input)