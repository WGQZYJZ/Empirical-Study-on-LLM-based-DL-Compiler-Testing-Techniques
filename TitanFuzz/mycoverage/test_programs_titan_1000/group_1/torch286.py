import torch
from torch import nn
from torch.autograd import Variable
_input_tensor = torch.rand(1, 3)
torch.Tensor.sin_(_input_tensor)