import torch
from torch import nn
from torch.autograd import Variable
_input_tensor = torch.rand(3, 3)
_sum_tensor = torch.Tensor.sum(_input_tensor, dim=None, keepdim=False, dtype=None)