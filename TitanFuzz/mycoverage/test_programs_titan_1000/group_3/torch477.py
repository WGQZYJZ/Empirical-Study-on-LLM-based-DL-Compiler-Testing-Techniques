import torch
from torch import nn
from torch.autograd import Variable
input = torch.tensor([[10, 20, 30, 40], [50, 60, 70, 80]])
other = torch.tensor([[1, 2, 3, 4], [5, 6, 7, 8]])
output = torch.divide(input, other)