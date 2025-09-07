import torch
from torch import nn
from torch.autograd import Variable
_input_tensor = torch.randn(4)
_output_tensor = torch.Tensor.exp(_input_tensor)