import torch
from torch import nn
from torch.autograd import Variable
_input_tensor = torch.rand(2, 3, 4, 5)
_output_tensor = torch.Tensor.arctan(_input_tensor)