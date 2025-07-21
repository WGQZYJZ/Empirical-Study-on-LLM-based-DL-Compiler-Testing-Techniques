import torch
from torch import nn
from torch.autograd import Variable
_input_tensor = torch.randn(2, 3, 4)
_output_tensor = torch.Tensor.prod(_input_tensor, dim=1, keepdim=True)