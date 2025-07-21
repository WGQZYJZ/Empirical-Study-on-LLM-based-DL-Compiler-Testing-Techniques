import torch
from torch import nn
from torch.autograd import Variable
_input_tensor = torch.randn(2, 3, 4, 5)
_input_tensor_int = torch.Tensor.int(_input_tensor)
_input_tensor_long = torch.Tensor.long(_input_tensor)
_input_tensor_short = torch.Tensor.short(_input_tensor)