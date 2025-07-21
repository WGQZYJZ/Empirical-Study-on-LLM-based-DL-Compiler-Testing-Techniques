import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.randn(1, 3, 3)
relu6 = torch.nn.ReLU6(inplace=False)
output_data = relu6(input_data)