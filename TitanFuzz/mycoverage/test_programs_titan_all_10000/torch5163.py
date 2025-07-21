import torch
from torch import nn
from torch.autograd import Variable
_input_tensor = torch.randn(3, 3)
sinc_output = torch.Tensor.sinc(_input_tensor)