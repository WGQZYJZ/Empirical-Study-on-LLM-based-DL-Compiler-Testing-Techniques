import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.tensor([[0, 1, 0], [1, 0, 1]])
other = 2
output_tensor = torch.Tensor.bitwise_left_shift_(input_tensor, other)