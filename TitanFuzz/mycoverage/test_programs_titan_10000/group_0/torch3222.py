import torch
from torch import nn
from torch.autograd import Variable

input_tensor = torch.randn(4, 4)
divide_result = torch.Tensor.divide(input_tensor, 2)