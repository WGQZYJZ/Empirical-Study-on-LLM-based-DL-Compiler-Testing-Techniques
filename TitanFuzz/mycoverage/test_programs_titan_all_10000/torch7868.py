import torch
from torch import nn
from torch.autograd import Variable
_input_tensor = torch.randn(3, 3)
_input_tensor[(1, 1)] = float('nan')
_output_tensor = torch.Tensor.nanmean(_input_tensor, dim=None, keepdim=False, dtype=None)