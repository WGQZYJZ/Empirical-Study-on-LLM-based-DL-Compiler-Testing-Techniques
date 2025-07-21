import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.arange(1, 37).view(2, 3, 6)
output_data = torch.rot90(input_data, 1, dims=(0, 2))