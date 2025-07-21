import torch
from torch import nn
from torch.autograd import Variable
_input_tensor = torch.randn(2, 3, 4)
count_nonzero = torch.Tensor.count_nonzero(_input_tensor, dim=None)