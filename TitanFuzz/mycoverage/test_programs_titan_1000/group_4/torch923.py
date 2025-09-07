import torch
from torch import nn
from torch.autograd import Variable
_input_tensor = torch.randn(2, 3)
_output_tensor = torch.Tensor.exp(_input_tensor)
_input_tensor = torch.randn(2, 3)
_output_tensor = torch.Tensor.log(_input_tensor)
_input_tensor = torch.randn(2, 3)