import torch
from torch import nn
from torch.autograd import Variable
input_data = Variable(torch.randn(1, 1, 2, 2, 2))
dropout3d = torch.nn.Dropout3d(p=0.5, inplace=False)
output = dropout3d(input_data)