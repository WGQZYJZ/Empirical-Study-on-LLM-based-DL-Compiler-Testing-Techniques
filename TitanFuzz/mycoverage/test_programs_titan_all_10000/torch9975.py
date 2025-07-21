import torch
from torch import nn
from torch.autograd import Variable
_input_tensor = torch.randn(2, 3, 4)
_input_tensor[(0, 1, 2)] = float('nan')
_input_tensor[(1, 0, 0)] = float('nan')
_input_tensor[(1, 0, 1)] = float('nan')
_output_tensor = torch.Tensor.nansum(_input_tensor, dim=1, keepdim=False, dtype=None)