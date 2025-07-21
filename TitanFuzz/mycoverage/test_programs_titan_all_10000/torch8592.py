import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randn(3, 4)
mul_tensor = torch.Tensor.mul(input_tensor, 2)