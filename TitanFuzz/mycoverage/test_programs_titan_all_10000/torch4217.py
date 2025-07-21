import torch
from torch import nn
from torch.autograd import Variable
input = torch.randint(low=10, high=100, size=(4,))
other = torch.randint(low=10, high=100, size=(4,))
output = torch.gcd(input, other)