import torch
from torch import nn
from torch.autograd import Variable

input_tensor = torch.randn(2, 3, 4)
quantile = torch.Tensor.nanquantile(input_tensor, 0.5, dim=2)