import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.randn(100, 10)
split_data = torch.utils.data.random_split(input_data, [20, 80])