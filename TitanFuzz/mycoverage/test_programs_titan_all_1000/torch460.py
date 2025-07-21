import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.rand(1, 3)
output = torch.fmod(input_data, 2)