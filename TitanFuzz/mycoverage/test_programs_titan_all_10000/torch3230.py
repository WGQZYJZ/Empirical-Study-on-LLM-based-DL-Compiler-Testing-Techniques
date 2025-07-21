import torch
from torch import nn
from torch.autograd import Variable
_input_tensor = torch.randn(3, 5)
torch.Tensor.t_(_input_tensor)