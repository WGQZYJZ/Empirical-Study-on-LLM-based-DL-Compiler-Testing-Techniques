import torch
from torch import nn
from torch.autograd import Variable
_input_tensor = torch.randn(2, 3)
_other = torch.randn(2, 3)
_output_tensor = torch.Tensor.ge(_input_tensor, _other)