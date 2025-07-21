import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randint(low=0, high=100, size=(3, 3), dtype=torch.int8)
output_tensor = torch.Tensor.bitwise_right_shift_(input_tensor, 2)