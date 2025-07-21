import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.tensor([0.9, 1.4, 2.6, 3.5, 4.6, 5.9, 6.9, 7.5, 8.9, 9.5])
output = torch.round(input_data)
output = torch.round(input_data, out=None)