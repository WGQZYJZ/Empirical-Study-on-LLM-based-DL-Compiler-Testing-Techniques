import torch
from torch import nn
from torch.autograd import Variable

input_data = torch.rand(10, 10)
other_data = torch.rand(10, 10)
torch.special.gammaincc(input_data, other_data)