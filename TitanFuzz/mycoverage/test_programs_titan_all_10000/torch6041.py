import torch
from torch import nn
from torch.autograd import Variable
_input_tensor = torch.randn(1, 2, 3)
torch.Tensor.signbit(_input_tensor)