import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.randn(1, 1, 3, 3)
softshrink = torch.nn.Softshrink(lambd=0.5)
output_data = softshrink(input_data)