import torch
from torch import nn
from torch.autograd import Variable
_input_tensor = torch.randn(2, 3)
torch.Tensor.ne(_input_tensor, _input_tensor)
_input_tensor = torch.randn(2, 3)
torch.Tensor.lt(_input_tensor, _input_tensor)
_input_tensor = torch.randn(2, 3)