import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.rand(10)
output = torch.bartlett_window(window_length=10, periodic=True)