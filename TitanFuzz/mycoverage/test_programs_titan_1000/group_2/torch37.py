import torch
from torch import nn
from torch.autograd import Variable
_input_tensor = torch.rand((4, 3))
_output_tensor = torch.Tensor.cummin(_input_tensor, dim=1)