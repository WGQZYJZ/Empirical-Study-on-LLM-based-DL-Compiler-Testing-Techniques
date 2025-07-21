import torch
from torch import nn
from torch.autograd import Variable
_input_tensor = torch.rand(2, 3)
_fixed_tensor = torch.Tensor.fix(_input_tensor)