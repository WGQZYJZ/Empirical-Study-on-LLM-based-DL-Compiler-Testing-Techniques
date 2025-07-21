import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.randn(10)
torch.Tensor.erf_(input_data)