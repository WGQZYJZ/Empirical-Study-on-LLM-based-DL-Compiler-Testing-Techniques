import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.randn(3, 5, requires_grad=True)
softmax = torch.nn.Softmax(dim=1)
output = softmax(input_data)