import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.rand(5, 5)
arcsinh_data = torch.arcsinh(input_data)