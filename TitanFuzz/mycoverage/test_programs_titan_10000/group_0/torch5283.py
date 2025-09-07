import torch
from torch import nn
from torch.autograd import Variable

input_data = torch.randn(5)
output = torch.arccos(input_data)