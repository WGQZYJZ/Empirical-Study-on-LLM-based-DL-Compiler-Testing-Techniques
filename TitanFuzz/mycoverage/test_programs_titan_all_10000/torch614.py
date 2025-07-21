import torch
from torch import nn
from torch.autograd import Variable
_input = torch.randn(2, 3, 4)
_output = torch.Tensor.storage_offset(_input)