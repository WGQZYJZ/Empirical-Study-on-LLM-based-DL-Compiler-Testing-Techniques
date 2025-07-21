import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.randn(1, 1, 3, 5)
relu6 = torch.nn.ReLU6()
output = relu6(input_data)