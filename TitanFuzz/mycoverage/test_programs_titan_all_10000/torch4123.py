import torch
from torch import nn
from torch.autograd import Variable
input_data = Variable(torch.randn(5, 5, 5))
output_data = torch.nn.functional.dropout3d(input_data, p=0.5, training=True, inplace=False)