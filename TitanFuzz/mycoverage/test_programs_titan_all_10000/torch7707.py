import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.randn(1, 3, 32, 32)
flatten = torch.nn.Flatten()
output_data = flatten(input_data)