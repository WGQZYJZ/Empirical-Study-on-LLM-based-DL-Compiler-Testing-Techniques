import torch
from torch import nn
from torch.autograd import Variable
in_data = torch.randn(5)
out_data = torch.arcsinh(in_data)