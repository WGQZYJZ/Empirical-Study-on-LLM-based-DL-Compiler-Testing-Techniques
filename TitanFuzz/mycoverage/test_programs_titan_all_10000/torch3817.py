import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.randn(3, 3)
other_data = torch.randn(3, 3)
torch.fmax(input_data, other_data)