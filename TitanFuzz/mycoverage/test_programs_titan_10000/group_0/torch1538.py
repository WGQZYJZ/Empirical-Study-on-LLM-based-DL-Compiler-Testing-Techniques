import torch
from torch import nn
from torch.autograd import Variable

input_data = torch.randn(2, 3)
output_data = torch.fmax(input_data, torch.ones(2, 3))