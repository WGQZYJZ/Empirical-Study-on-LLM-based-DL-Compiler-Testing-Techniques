import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.randn(10, 20)
result = torch.jit.isinstance(input_data, torch.Tensor)