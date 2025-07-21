import torch
from torch import nn
from torch.autograd import Variable
input = torch.tensor([[1, 2], [3, 4]])
output = torch.ravel(input)