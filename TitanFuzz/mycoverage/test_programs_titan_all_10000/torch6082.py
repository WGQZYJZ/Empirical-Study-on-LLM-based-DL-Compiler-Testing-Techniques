import torch
from torch import nn
from torch.autograd import Variable
_input_tensor = torch.rand(3, 3)
_output_tensor = torch.Tensor.prod(_input_tensor, dim=0, keepdim=True)