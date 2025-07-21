import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.randn((1, 3, 3))
threshold_layer = torch.nn.Threshold(0.5, 0)
output_data = threshold_layer(input_data)