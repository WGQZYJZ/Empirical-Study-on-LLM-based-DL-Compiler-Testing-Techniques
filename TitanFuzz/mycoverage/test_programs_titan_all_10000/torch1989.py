import torch
from torch import nn
from torch.autograd import Variable
_input_tensor = torch.randn(1, 3, 3)
torch.Tensor.mvlgamma(_input_tensor, 1)