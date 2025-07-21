import torch
from torch import nn
from torch.autograd import Variable
_input_tensor = torch.randn(2, 4, 4)
_output_tensor = torch.Tensor.ravel(_input_tensor)