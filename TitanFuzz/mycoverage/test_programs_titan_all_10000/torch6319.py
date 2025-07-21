import torch
from torch import nn
from torch.autograd import Variable
_input_tensor = torch.rand(2, 3, 5)
_storage_offset = torch.Tensor.storage_offset(_input_tensor)