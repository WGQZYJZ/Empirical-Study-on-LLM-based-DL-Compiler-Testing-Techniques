import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.rand(4, 4)
frac_result = torch.Tensor.frac_(input_tensor)