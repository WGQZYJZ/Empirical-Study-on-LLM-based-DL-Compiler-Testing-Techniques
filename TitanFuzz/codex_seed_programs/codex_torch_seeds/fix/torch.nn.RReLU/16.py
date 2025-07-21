'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.RReLU\ntorch.nn.RReLU(lower=0.125, upper=0.3333333333333333, inplace=False)\n'
import torch
from torch.autograd import Variable
import torch.nn as nn
input_data = Variable(torch.randn(5, 3))
relu = nn.RReLU(lower=0.125, upper=0.3333333333333333, inplace=False)
output = relu(input_data)
print(output)