import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randn(2, 2)
result_tensor = torch.Tensor.matrix_power(input_tensor, 2)