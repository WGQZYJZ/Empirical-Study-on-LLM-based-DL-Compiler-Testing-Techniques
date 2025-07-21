import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.rand(10)
output = torch.kaiser_window(10, periodic=True, beta=12.0)