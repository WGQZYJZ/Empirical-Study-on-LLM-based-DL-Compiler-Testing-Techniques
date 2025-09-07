import torch
from torch import nn
from torch.autograd import Variable
input = torch.randint(low=0, high=10, size=(2, 2), dtype=torch.int32)
output = torch.randint_like(input, low=0, high=10)