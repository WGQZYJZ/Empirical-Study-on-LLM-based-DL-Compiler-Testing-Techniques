import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randn(1, 3, 3)
imag_tensor = torch.Tensor.imag(input_tensor)