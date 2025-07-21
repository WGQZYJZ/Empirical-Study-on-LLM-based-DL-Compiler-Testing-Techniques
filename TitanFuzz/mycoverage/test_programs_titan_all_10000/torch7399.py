import torch
from torch import nn
from torch.autograd import Variable
if True:
    input_tensor = torch.randn(2, 3, 4)
    print(f'Input Tensor: {input_tensor}')
    print(f'Real part of input tensor: {torch.Tensor.real(input_tensor)}')