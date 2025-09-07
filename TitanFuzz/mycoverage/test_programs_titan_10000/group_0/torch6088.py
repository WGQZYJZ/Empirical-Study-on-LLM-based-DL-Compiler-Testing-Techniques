import torch
from torch import nn
from torch.autograd import Variable

_input_tensor = torch.randn(5, 3)
output_tensor = torch.Tensor.tan(_input_tensor)