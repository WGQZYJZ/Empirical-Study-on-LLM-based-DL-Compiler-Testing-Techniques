import torch
from torch import nn
from torch.autograd import Variable
_input_tensor = torch.randn(2, 2)
_is_shared = torch.Tensor.is_shared(_input_tensor)