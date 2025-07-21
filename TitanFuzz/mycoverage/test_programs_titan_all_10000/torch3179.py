import torch
from torch import nn
from torch.autograd import Variable
_input_tensor = torch.randn(10)
output = torch.Tensor.new_tensor(_input_tensor, data=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10])