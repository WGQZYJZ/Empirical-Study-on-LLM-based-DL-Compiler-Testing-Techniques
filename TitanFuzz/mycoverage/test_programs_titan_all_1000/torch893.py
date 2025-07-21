import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.arange(0, 100)
output = torch.utils.data.Subset(input_data, [0, 2, 4, 6, 8])