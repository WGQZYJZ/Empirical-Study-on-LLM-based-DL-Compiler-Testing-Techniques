import torch
from torch import nn
from torch.autograd import Variable
_input = torch.randn(2, 3, 4, 5)
_input_tensor = torch.Tensor.int(_input)