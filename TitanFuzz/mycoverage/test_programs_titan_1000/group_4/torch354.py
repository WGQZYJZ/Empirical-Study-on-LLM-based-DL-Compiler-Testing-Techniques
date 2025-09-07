import torch
from torch import nn
from torch.autograd import Variable
_input_tensor = torch.randn(3, 3)
_output_tensor = torch.Tensor.any(_input_tensor, dim=None, keepdim=False)