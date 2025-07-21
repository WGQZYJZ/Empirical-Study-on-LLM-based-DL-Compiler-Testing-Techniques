import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randint(0, 2, (2, 3), dtype=torch.int8)
input_tensor = torch.randint(0, 2, (2, 3), dtype=torch.int8)
output_tensor = torch.Tensor.bitwise_left_shift(input_tensor, 2)