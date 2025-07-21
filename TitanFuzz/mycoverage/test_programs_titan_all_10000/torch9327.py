import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.randn(4, 4)
output = torch.triu(input_data)
output = torch.triu(input_data, diagonal=1)