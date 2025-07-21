'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.abs\ntorch.abs(input, *, out=None)\n'
import torch
from torch.autograd import Variable
input = Variable(torch.randn(1, 3))
print(input)
output = torch.abs(input)
print(output)