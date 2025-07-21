import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.randn(4, 4)
output_data = torch.tril(input_data)