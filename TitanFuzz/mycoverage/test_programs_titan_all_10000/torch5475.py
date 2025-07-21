import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.arange(0, 10)
split_data = torch.split(input_data, 3)
input_data = torch.arange(0, 9)
input_data = input_data.view(1, 1, 3, 3)
squeeze_data = torch.squeeze(input_data)
input_data1 = torch.arange(0, 3)
input_data2 = torch.arange(3, 6)