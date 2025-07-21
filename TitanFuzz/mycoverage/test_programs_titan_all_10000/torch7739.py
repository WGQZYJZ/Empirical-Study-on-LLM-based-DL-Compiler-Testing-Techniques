import torch
from torch import nn
from torch.autograd import Variable
_input_tensor = torch.randn(2, 3)
_size = (4, 5)
_fill_value = 1.0
_output_tensor = torch.Tensor.new_full(_input_tensor, _size, _fill_value)