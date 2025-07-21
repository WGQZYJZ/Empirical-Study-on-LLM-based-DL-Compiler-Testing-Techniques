import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.arange(1, 17).view(4, 4)
torch.hsplit(input_data, 2)