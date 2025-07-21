import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.arange(1, 11)
output = torch.log10(input_data)