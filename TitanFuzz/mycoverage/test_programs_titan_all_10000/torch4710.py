import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.randn(1, 3, 10, 10, 10)
dropout3d = torch.nn.Dropout3d(p=0.5)
output = dropout3d(input_data)