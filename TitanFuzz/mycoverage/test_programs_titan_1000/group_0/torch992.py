import torch
from torch import nn
from torch.autograd import Variable
input = torch.tensor([[0, 1, 2], [3, 4, 5], [6, 7, 8]])
output = torch.squeeze(input)