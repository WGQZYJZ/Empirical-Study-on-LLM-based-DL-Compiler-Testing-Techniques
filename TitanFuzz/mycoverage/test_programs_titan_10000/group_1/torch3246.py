import torch
from torch import nn
from torch.autograd import Variable

_input_tensor = torch.rand(5, 5)
torch.Tensor.matrix_exp(_input_tensor)