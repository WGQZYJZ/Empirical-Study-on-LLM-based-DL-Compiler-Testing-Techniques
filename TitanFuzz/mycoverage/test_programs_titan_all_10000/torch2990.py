import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randn(3, 3)
input_tensor[(0, 0)] = float('nan')
input_tensor[(0, 1)] = float('nan')
input_tensor[(1, 1)] = float('nan')
input_tensor[(2, 1)] = float('nan')
input_tensor[(2, 2)] = float('nan')
result = torch.Tensor.nanmean(input_tensor, dim=0)