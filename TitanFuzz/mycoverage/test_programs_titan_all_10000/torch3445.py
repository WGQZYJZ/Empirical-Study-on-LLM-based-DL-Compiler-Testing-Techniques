import torch
from torch import nn
from torch.autograd import Variable
_input_tensor = torch.rand(1, 3, 4, 4)
torch.Tensor.t_(_input_tensor)