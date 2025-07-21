import torch
from torch import nn
from torch.autograd import Variable
_input_tensor = torch.randn(2, 3)
torch.Tensor.new_tensor(_input_tensor, data=None, dtype=None, device=None, requires_grad=False)