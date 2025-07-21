import torch
from torch import nn
from torch.autograd import Variable
_input_tensor = torch.randn(3, 3)
torch.Tensor.fix_(_input_tensor)