import torch
from torch import nn
from torch.autograd import Variable
_input_tensor = torch.rand(1, 3, 4, 5)
acosh_output = torch.Tensor.acosh_(_input_tensor)