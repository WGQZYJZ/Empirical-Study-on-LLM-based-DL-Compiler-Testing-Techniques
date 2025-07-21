import torch
from torch import nn
from torch.autograd import Variable
input_data_1 = torch.randn(3, 2)
input_data_2 = torch.randn(3, 2)
bilinear_model = torch.nn.Bilinear(2, 2, 1, bias=True)
output = bilinear_model(input_data_1, input_data_2)