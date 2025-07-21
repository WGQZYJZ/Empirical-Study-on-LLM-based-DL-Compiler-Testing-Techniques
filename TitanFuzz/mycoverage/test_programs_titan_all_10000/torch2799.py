import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.randn(20, 16)
dropout_layer = torch.nn.Dropout(p=0.5, inplace=False)
output_data = dropout_layer(input_data)