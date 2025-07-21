import torch
from torch import nn
from torch.autograd import Variable
input_data = Variable(torch.randn(2, 3))
sigmoid_layer = torch.nn.SiLU(inplace=False)
sigmoid_output = sigmoid_layer(input_data)