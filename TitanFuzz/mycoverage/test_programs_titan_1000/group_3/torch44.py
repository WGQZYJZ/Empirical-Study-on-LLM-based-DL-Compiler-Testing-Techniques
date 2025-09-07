import torch
from torch import nn
from torch.autograd import Variable
_input_tensor = torch.rand(2, 3)
is_set_to_result = torch.Tensor.is_set_to(_input_tensor, _input_tensor)