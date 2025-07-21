import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.randint(0, 2, (3, 3), dtype=torch.uint8)
output = torch.bitwise_right_shift(input_data, 2)