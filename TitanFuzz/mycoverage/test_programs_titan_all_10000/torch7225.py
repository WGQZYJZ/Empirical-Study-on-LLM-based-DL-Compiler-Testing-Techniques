import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.randn(1, 2, 3)
shrink = torch.nn.Softshrink(lambd=0.5)
output_data = shrink(input_data)