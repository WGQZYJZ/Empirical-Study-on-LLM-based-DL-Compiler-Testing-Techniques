import torch
from torch import nn
from torch.autograd import Variable
input = torch.tensor([[1, 2, 3], [4, 5, 6]], dtype=torch.int64)
other = torch.tensor([[1, 2, 3], [4, 5, 6]], dtype=torch.int64)
torch.bitwise_left_shift(input, other)