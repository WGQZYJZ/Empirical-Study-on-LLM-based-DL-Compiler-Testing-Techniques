import torch
from torch import nn
from torch.autograd import Variable
_input_tensor = torch.randn(4, 5)
_output_tensor = torch.Tensor.narrow_copy(_input_tensor, 1, 1, 2)