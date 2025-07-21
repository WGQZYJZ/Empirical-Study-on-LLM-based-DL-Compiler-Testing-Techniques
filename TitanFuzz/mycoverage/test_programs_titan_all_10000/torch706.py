import torch
from torch import nn
from torch.autograd import Variable
_input_tensor = torch.rand(3, 3)
_var = torch.Tensor.var(_input_tensor, dim=None, unbiased=True, keepdim=False)