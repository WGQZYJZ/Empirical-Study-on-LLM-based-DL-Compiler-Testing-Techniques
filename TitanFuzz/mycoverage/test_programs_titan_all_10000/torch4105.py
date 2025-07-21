import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.rand(2, 3)
output_data = torch.fmod(input_data, 2)