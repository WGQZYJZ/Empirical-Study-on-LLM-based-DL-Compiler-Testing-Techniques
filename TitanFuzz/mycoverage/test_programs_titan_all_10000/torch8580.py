import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.arange(0, 9, 1).view(3, 3)
result_data = torch.flip(input_data, [1])
result_data = torch.flip(input_data, [0])