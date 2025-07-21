import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.randn(1, 2, 3)
tanhshrink = torch.nn.Tanhshrink()
output = tanhshrink(input_data)