import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.arange(1, 11).view(2, 5)
result = torch.flipud(input_data)