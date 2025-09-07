import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.Tensor([[1, 2, 3], [4, 5, 6]])
other = 1
output_tensor = torch.Tensor.bitwise_left_shift_(input_tensor, other)