import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.randn(1, 1, 4, 4)
threshold = torch.nn.Threshold(0.5, 0)
output = threshold(input_data)
input_data = torch.randn(1, 1, 4, 4)
relu = torch.nn.ReLU()
output = relu(input_data)