import torch
from torch import nn
from torch.autograd import Variable
if True:
    input_tensor = torch.randn(1, 3, 3)
    print('input_tensor:', input_tensor)
    output_tensor = torch.Tensor.arccos_(input_tensor)
    print('output_tensor:', output_tensor)