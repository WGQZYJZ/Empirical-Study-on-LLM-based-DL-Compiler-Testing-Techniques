import torch
from torch import nn
from torch.autograd import Variable
input = torch.tensor([24, 60], dtype=torch.int32)
out = torch.gcd(input[0], input[1])