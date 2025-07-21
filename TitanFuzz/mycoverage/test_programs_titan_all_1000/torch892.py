import torch
from torch import nn
from torch.autograd import Variable
_input_tensor = torch.rand(4, 4)
_negative_tensor = torch.Tensor.negative(_input_tensor)