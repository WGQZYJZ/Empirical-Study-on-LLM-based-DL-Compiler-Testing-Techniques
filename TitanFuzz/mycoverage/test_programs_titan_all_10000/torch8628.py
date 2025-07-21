import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.randn(3, 3)
threshold = torch.nn.Threshold(0.5, 0.5)
output_data = threshold(input_data)