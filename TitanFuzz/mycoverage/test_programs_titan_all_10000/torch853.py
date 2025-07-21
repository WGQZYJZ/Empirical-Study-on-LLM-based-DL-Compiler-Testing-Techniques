import torch
from torch import nn
from torch.autograd import Variable
_input_tensor = torch.rand(10, 10)
_max_output = torch.Tensor.max(_input_tensor, dim=None, keepdim=False)