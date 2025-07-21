import torch
from torch import nn
from torch.autograd import Variable
_input_tensor = torch.randn(3, 4)
_output_tensor = torch.Tensor.amax(_input_tensor, dim=None, keepdim=False)