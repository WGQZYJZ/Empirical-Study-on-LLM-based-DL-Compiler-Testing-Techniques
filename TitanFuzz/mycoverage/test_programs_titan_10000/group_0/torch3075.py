import torch
from torch import nn
from torch.autograd import Variable

input_tensor = torch.randn(1, 3, 2)
result = torch.Tensor.floor_divide_(input_tensor, 2)