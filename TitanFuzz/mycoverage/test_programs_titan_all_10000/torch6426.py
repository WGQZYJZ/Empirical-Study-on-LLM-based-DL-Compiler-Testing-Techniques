import torch
from torch import nn
from torch.autograd import Variable
input = torch.randint(0, 2, (2, 3), dtype=torch.int8)
other = torch.randint(0, 2, (2, 3), dtype=torch.int8)
torch.bitwise_left_shift(input, other)