import torch
from torch import nn
from torch.autograd import Variable
_input_tensor = torch.randn(1, 10)
_output_tensor = torch.Tensor.sinc_(_input_tensor)