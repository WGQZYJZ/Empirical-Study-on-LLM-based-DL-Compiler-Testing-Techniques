import torch
from torch import nn
from torch.autograd import Variable
_input_tensor = torch.rand(3, 3)
_result = torch.Tensor.sqrt(_input_tensor)
_result = torch.sqrt(_input_tensor)