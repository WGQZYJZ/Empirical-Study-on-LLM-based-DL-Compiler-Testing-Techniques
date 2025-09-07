import torch
from torch import nn
from torch.autograd import Variable

_input_tensor = torch.rand(3, 3)
_output_tensor = torch.Tensor.conj(_input_tensor)