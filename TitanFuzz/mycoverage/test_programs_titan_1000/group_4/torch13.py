import torch
from torch import nn
from torch.autograd import Variable
_input_tensor = torch.randn(3, 3)
_output_tensor = torch.Tensor.as_subclass(_input_tensor, torch.Tensor)