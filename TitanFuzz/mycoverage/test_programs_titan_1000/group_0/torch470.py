import torch
from torch import nn
from torch.autograd import Variable
_input_tensor = torch.randn(10, 10)
torch.Tensor.fix_(_input_tensor)