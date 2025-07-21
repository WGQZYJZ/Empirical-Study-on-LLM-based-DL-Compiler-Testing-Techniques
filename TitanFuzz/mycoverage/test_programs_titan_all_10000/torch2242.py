import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.rand(10, 10)
floor_divide_tensor = torch.Tensor.floor_divide(input_tensor, 2)