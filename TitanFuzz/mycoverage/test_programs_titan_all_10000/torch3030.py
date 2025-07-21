import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.tensor([[2, 3, 4], [5, 6, 7]])
exponent = 2
output_tensor = torch.Tensor.float_power_(input_tensor, exponent)