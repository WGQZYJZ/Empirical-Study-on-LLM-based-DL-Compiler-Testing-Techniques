import torch
from torch import nn
from torch.autograd import Variable
_input_tensor = torch.randn(4, 3)
_output_tensor = torch.Tensor.new_tensor(_input_tensor, data=_input_tensor, dtype=None, device=None, requires_grad=False)