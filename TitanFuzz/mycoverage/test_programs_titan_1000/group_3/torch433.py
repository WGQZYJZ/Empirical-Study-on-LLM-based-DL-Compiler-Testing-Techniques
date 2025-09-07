import torch
from torch import nn
from torch.autograd import Variable
input = torch.randint(1, 10, (3, 3), dtype=torch.int32)
other = torch.randint(1, 10, (3, 3), dtype=torch.int32)
output = torch.lcm(input, other)