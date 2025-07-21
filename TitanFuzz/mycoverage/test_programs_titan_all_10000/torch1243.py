import torch
from torch import nn
from torch.autograd import Variable
_input_tensor = torch.randn(1, 2, 3, 4)
_output_tensor = torch.Tensor.log2(_input_tensor)