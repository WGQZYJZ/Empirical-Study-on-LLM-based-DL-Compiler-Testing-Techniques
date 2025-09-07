import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randn(4, 4)
result = torch.Tensor.matrix_power(input_tensor, 2)