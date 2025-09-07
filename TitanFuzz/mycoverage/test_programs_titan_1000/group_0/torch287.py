import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.randn(1, 2, 3, 4, 5)
dropout = torch.nn.Dropout3d(p=0.5, inplace=False)
output_data = dropout(input_data)