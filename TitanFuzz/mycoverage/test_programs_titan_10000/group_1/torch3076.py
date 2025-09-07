import torch
from torch import nn
from torch.autograd import Variable

_input_tensor = torch.rand(3, 3)
_storage_offset = torch.Tensor.storage_offset(_input_tensor)