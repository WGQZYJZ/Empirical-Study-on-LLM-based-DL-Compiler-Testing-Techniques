import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.rand(100, 1000)
output_data = torch.nn.functional.dropout(input_data, p=0.5, training=True, inplace=False)