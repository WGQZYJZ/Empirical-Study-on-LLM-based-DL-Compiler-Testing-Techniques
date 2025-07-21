import torch
from torch import nn
from torch.autograd import Variable
_input_tensor = torch.randn(2, 3)
torch.Tensor.fix(_input_tensor)