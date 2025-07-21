import torch
from torch import nn
from torch.autograd import Variable
input = torch.tensor([[1, 1, 1], [0, 0, 0]], dtype=torch.bool)
output = torch.logical_not(input)