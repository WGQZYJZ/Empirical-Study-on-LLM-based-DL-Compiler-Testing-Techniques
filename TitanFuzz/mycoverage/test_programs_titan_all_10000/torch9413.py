import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.randn(100)
torch.frexp(input_data)