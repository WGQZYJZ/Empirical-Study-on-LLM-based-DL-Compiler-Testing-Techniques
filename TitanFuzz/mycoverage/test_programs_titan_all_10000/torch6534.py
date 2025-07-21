import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randn(2, 2)
output_tensor = torch.Tensor.matrix_exp(input_tensor)