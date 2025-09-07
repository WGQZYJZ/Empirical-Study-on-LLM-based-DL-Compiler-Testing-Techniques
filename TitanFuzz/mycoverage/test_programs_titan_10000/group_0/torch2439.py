import torch
from torch import nn
from torch.autograd import Variable

input = torch.rand(5, 3)
index = torch.tensor([1, 2])
output = torch.take(input, index)