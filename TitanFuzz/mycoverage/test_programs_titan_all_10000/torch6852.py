import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.randn(2, 3, 4)
output_data = torch.flatten(input_data)