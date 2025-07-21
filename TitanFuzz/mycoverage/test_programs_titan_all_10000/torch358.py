import torch
from torch import nn
from torch.autograd import Variable
_input_tensor = torch.rand(3, 3)
A = torch.rand(3, 3)
torch.Tensor.lstsq(_input_tensor, A)