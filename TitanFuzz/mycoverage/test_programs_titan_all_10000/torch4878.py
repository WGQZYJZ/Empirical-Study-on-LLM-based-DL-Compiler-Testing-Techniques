import torch
from torch import nn
from torch.autograd import Variable
_input_tensor = torch.randn(4, 4)
torch.Tensor.mode(_input_tensor, dim=None, keepdim=False)