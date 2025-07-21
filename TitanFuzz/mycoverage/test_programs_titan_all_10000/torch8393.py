import torch
from torch import nn
from torch.autograd import Variable
_input_tensor = torch.randn(3, 3)
torch.Tensor.fill_(_input_tensor, value=0.0)