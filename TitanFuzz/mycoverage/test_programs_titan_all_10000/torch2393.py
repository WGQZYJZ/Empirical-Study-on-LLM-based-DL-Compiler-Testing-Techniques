import torch
from torch import nn
from torch.autograd import Variable
input = torch.randint(0, 2, (3, 3), dtype=torch.int32)
other = torch.randint(0, 2, (3, 3), dtype=torch.int32)
out = torch.bitwise_left_shift(input, other)