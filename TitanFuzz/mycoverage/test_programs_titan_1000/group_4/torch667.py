import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.randn(5, 5)
signbit_data = torch.signbit(input_data)