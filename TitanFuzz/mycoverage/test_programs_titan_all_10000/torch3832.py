import torch
from torch import nn
from torch.autograd import Variable
_input_tensor = torch.randn(2, 3)
_device = torch.Tensor.device(_input_tensor)