import torch
from torch import nn
from torch.autograd import Variable
_input_tensor = torch.randn(1, 3, 4, 4)
_output_tensor = torch.Tensor.atanh(_input_tensor)