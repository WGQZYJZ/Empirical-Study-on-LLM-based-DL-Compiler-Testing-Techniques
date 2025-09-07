import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randn(1, 3, 4, 5)
arcsinh_output = torch.Tensor.arcsinh(input_tensor)