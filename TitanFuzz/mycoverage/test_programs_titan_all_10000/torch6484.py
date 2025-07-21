import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.randn(1, 2, 3, 4, 5)
result = torch.Tensor.imag(input_data)