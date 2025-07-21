import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.randn(1, 5)
output_data = torch.ones(input_data.size())