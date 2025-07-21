import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randn(10)
quantile_tensor = torch.Tensor.quantile(input_tensor, 0.5)