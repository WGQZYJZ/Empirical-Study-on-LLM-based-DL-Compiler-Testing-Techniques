import torch
from torch import nn
from torch.autograd import Variable
_input_tensor = torch.rand(10, 10)
_isfinite = torch.Tensor.isfinite(_input_tensor)