import torch
from torch import nn
from torch.autograd import Variable
_input_tensor = torch.rand((10,))
_device = torch.Tensor.device(_input_tensor)