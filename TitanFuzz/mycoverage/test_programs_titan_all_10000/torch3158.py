import torch
from torch import nn
from torch.autograd import Variable
_input_tensor = torch.rand(3, 3)
_output_tensor = torch.Tensor.square(_input_tensor)
_output_tensor = torch.Tensor.sum(_input_tensor, dim=0)