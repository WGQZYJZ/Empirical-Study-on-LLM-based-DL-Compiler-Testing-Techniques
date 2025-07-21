import torch
from torch import nn
from torch.autograd import Variable
_input_tensor = torch.rand((1, 2, 3))
torch.Tensor.floor(_input_tensor)