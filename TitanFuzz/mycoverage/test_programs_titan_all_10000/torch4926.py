import torch
from torch import nn
from torch.autograd import Variable
_input_tensor = torch.randn(10, 10)
_output_tensor = torch.Tensor.nonzero(_input_tensor, as_tuple=False)