import torch
from torch import nn
from torch.autograd import Variable

input_data = torch.randn(3, 4)
torch.cummax(input_data, dim=1)