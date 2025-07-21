import torch
from torch import nn
from torch.autograd import Variable
if True:
    _input_tensor = torch.randn(4, 4)
    _output_tensor = torch.Tensor.round(_input_tensor)
    print('input_tensor:', _input_tensor)
    print('output_tensor:', _output_tensor)