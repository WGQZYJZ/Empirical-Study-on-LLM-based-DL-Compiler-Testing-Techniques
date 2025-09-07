import torch
from torch import nn
from torch.autograd import Variable
_input_tensor = torch.randn(1, 3, 3, 3)
_output_tensor = torch.Tensor.floor(_input_tensor)