'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.dropout2d\ntorch.nn.functional.dropout2d(input, p=0.5, training=True, inplace=False)\n'
import torch
from torch.autograd import Variable
from torch.nn.functional import dropout2d
import torch
input = Variable(torch.randn(1, 1, 4, 4))
print(input)
output = dropout2d(input, p=0.5, training=True, inplace=False)
print(output)