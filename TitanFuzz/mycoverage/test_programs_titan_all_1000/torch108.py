import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.tensor([1, 2, 3, 4])
other_data = torch.tensor([2, 3, 4, 5])
output = torch.bitwise_left_shift(input_data, other_data)