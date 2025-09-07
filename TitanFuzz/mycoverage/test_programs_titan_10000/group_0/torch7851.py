import torch
from torch import nn
from torch.autograd import Variable

input = torch.randn(10, 3)
output = torch.tensor_split(input, 5, 0)