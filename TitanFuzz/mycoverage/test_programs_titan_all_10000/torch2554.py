import torch
from torch import nn
from torch.autograd import Variable
_input_tensor = torch.rand(4, 4)
_output_tensor = torch.Tensor.cos(_input_tensor)