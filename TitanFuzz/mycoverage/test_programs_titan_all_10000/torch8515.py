import torch
from torch import nn
from torch.autograd import Variable
_input_tensor = torch.randn(3, 4)
_output_tensor = torch.Tensor.sgn(_input_tensor)