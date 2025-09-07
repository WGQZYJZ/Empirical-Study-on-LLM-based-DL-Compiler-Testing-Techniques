import torch
from torch import nn
from torch.autograd import Variable

input_tensor = torch.rand(2, 2)
output_tensor = torch.Tensor.matrix_power(input_tensor, 2)