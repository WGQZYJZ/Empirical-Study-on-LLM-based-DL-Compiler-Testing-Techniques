import torch
from torch import nn
from torch.autograd import Variable
_input_tensor = torch.rand(3, 4)
torch.Tensor.frac(_input_tensor)