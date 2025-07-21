import torch
from torch import nn
from torch.autograd import Variable
input = torch.randint(10, (3, 3), dtype=torch.float)
output = torch.randint_like(input, low=0, high=10)