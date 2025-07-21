import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.randn(10, 20)
output = torch.sqrt(input_data)