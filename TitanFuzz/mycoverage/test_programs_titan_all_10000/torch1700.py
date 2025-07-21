import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.arange(0, 24).view(2, 3, 4)
output_data = torch.flip(input_data, dims=[0])