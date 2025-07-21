import torch
from torch import nn
from torch.autograd import Variable
_input_tensor = torch.rand(2, 3)
_data = [1, 2, 3, 4, 5, 6]
_dtype = torch.float32
_device = torch.device('cpu')
_requires_grad = True
_output_tensor = torch.Tensor.new_tensor(_input_tensor, _data, _dtype, _device, _requires_grad)