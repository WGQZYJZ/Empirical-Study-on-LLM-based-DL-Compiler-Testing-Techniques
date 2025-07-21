import torch
from torch import nn
from torch.autograd import Variable
_input_tensor = torch.randn(2, 3, 3)
_output_tensor = torch.Tensor.det(_input_tensor)