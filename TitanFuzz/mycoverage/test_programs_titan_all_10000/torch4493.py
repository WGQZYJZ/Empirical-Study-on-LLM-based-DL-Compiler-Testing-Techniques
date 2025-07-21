import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.rand(1, 3)
result = torch.Tensor.floor_divide(input_tensor, 2)