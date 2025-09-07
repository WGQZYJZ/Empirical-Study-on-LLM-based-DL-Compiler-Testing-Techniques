import torch
from torch import nn
from torch.autograd import Variable

input_data = torch.randn(1, 2, 3, 4)
output = torch.special.psi(input_data)