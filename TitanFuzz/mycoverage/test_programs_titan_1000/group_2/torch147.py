import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.linspace(1, 10, steps=10)
other_data = torch.linspace(1, 10, steps=10)
output = torch.igammac(input_data, other_data)