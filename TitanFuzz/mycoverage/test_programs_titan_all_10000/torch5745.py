import torch
from torch import nn
from torch.autograd import Variable
_input_tensor = torch.randn(3, 2, 5)
_output_tensor = torch.Tensor.byte(_input_tensor)