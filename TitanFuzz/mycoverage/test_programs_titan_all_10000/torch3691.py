import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.randn(1, 3, 5, 5, 5)
dropout3d = torch.nn.Dropout3d(p=0.5, inplace=False)
output_data = dropout3d(input_data)