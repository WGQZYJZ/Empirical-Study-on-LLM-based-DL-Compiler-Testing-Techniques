import torch
from torch import nn
from torch.autograd import Variable
_input_tensor = torch.rand(2, 3, 4)
_output_tensor = torch.Tensor.count_nonzero(_input_tensor, dim=None)