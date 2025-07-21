import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.randn(2, 3)
relu6 = torch.nn.ReLU6()
output = relu6(input_data)