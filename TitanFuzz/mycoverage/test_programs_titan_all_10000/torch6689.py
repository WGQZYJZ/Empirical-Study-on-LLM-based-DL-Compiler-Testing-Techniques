import torch
from torch import nn
from torch.autograd import Variable
_input_tensor = torch.randn(5, 5)
torch.Tensor.zero_(_input_tensor)