import torch
from torch import nn
from torch.autograd import Variable

_input_tensor = torch.rand(3, 3)
torch.Tensor.sqrt_(_input_tensor)