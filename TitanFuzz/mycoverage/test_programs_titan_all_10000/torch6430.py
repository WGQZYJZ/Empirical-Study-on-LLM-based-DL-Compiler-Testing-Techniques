import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.arange(9)
output_data = torch.chunk(input_data, 3, dim=0)