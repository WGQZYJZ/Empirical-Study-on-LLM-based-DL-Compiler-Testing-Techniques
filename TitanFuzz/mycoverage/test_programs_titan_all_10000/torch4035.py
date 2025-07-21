import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randn(10)
result = torch.Tensor.floor_divide(input_tensor, 5)