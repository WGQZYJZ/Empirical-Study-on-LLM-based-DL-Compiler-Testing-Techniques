'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.Hardsigmoid\ntorch.nn.Hardsigmoid(inplace=False)\n'
import torch
from torch.autograd import Variable
import torch
input = Variable(torch.randn(2, 3))
output = torch.nn.Hardsigmoid(inplace=False)(input)
print(output)