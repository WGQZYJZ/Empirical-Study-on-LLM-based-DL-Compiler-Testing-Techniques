import torch
from torch import nn
from torch.autograd import Variable
input = torch.arange(9, dtype=torch.float32).reshape(3, 3)
output = torch.roll(input, 1, dims=1)