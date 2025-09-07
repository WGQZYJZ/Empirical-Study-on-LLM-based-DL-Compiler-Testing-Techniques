import torch
from torch import nn
from torch.autograd import Variable

input = torch.tensor([[1, 1, 1, 1], [2, 2, 2, 2], [3, 3, 3, 3], [4, 4, 4, 4]])
output = torch.mode(input, dim=0)