import torch
from torch import nn
from torch.autograd import Variable
input = torch.randint(1, 100, (5, 5), dtype=torch.long)
other = torch.randint(1, 100, (5, 5), dtype=torch.long)
out = torch.gcd(input, other)