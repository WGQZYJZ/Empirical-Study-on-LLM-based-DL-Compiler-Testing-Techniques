import torch
from torch import nn
from torch.autograd import Variable
_input_tensor = torch.randn(1, 2, 3, 4)
out = torch.Tensor.as_subclass(_input_tensor, torch.Tensor)