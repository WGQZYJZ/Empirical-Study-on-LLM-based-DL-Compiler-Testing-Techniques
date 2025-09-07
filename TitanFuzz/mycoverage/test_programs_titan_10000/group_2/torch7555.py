import torch
from torch import nn
from torch.autograd import Variable

input_data = torch.randn(2, 3)
softmax = torch.nn.Softmax()
output = softmax(input_data)