import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.ones(1, 1, 4, 4)
dropout = torch.nn.Dropout2d(p=0.5, inplace=False)
output = dropout(input_data)