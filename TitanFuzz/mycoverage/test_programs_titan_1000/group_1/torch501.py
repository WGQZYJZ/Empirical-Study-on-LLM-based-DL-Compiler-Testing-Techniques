import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.rand(3, 5)
output_data = torch.abs(input_data)