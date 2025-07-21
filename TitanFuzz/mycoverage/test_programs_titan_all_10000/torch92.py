import torch
from torch import nn
from torch.autograd import Variable
_input_tensor = torch.rand(4, 3)
torch.Tensor.geometric_(_input_tensor, 0.5)