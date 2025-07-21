import torch
from torch import nn
from torch.autograd import Variable
_input_tensor = torch.randn(1, 2, 3)
_fill_value = 1
_dtype = torch.int32
_requires_grad = True
_output_tensor = torch.Tensor.new_full(_input_tensor, _fill_value, _dtype, _device, _requires_grad)