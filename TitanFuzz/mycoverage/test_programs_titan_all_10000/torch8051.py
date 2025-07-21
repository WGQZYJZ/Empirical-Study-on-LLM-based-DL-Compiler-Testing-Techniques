import torch
from torch import nn
from torch.autograd import Variable
input = torch.randint(low=0, high=10, size=(5,), dtype=torch.int32)
result = torch.bitwise_right_shift(input, 2)