import torch
from torch import nn
from torch.autograd import Variable
_input_tensor = torch.randn(3, 3)
torch.Tensor.storage(_input_tensor)