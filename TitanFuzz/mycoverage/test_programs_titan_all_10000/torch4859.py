import torch
from torch import nn
from torch.autograd import Variable
_input_tensor = torch.rand(1, 3, 3)
_output_tensor = torch.Tensor.arctan(_input_tensor)