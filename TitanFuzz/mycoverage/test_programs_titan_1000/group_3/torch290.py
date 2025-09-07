import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.randint(low=0, high=100, size=(1,), dtype=torch.int8)
output_data = torch.bitwise_right_shift(input_data, 2, out=None)