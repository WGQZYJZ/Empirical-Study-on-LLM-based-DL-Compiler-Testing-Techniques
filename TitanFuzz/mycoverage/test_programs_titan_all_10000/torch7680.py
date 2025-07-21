import torch
from torch import nn
from torch.autograd import Variable
_input_tensor = torch.rand(10, 10)
torch.Tensor.q_zero_point(_input_tensor)