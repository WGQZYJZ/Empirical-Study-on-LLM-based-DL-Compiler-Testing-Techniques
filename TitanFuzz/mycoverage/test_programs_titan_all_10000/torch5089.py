import torch
from torch import nn
from torch.autograd import Variable
_input_tensor = torch.randn(10, dtype=torch.float32)
_real_tensor = torch.Tensor.real(_input_tensor)