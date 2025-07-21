import torch
from torch import nn
from torch.autograd import Variable
_input_tensor = torch.randn(1, 2, 3)
_output_tensor = torch.Tensor.square(_input_tensor)