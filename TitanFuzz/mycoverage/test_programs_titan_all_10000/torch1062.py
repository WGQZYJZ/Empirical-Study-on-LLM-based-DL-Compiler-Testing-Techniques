import torch
from torch import nn
from torch.autograd import Variable
_input_tensor = torch.rand(2, 3)
new_tensor = torch.Tensor.new_tensor(_input_tensor, data=None, dtype=None, device=None, requires_grad=False)