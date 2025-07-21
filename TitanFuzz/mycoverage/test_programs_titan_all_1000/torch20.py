import torch
from torch import nn
from torch.autograd import Variable
_input_tensor = torch.randn(2, 3, 5)
torch.Tensor.pinverse(_input_tensor)