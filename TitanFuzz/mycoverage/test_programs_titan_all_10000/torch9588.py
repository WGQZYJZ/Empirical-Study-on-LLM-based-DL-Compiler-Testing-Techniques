import torch
from torch import nn
from torch.autograd import Variable
input = torch.tensor([[True, True], [True, False], [False, True], [False, False]], dtype=torch.bool)
other = torch.tensor([[True, False], [True, False], [False, True], [False, False]], dtype=torch.bool)
output = torch.logical_and(input, other)