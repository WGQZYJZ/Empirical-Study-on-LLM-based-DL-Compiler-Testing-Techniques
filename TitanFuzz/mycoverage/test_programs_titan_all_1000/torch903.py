import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.randn(5)
output_data = torch.sign(input_data)