import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.rand(1000, 1000)
out_tensor = torch.Tensor.erf_(input_tensor)