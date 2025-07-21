import torch
from torch import nn
from torch.autograd import Variable
_input_tensor = torch.rand(4, 4)
torch.Tensor.fix_(_input_tensor)