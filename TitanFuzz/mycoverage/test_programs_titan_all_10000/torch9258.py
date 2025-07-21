import torch
from torch import nn
from torch.autograd import Variable
_input_tensor = torch.randn(2, 2)
_output_tensor = torch.Tensor.fix(_input_tensor)