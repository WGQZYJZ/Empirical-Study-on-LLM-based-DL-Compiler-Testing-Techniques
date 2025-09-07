import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randn(4, 4)
value = 2
divided_tensor = torch.Tensor.true_divide(input_tensor, value)