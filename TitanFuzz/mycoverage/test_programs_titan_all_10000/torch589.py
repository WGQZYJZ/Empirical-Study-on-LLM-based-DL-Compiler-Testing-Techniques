import torch
from torch import nn
from torch.autograd import Variable
_input_tensor = torch.rand(5, 3)
_output_tensor = torch.Tensor.multiply_(_input_tensor, 2)