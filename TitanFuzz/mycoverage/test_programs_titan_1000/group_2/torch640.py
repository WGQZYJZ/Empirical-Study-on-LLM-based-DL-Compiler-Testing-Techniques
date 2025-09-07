import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.randn(3, 3)
modulus_data = torch.fmod(input_data, 2)