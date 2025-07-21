'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.igammac\ntorch.igammac(input, other, *, out=None)\n'
import torch
from torch.autograd import Variable
input = Variable(torch.randn(2, 3))
other = Variable(torch.randn(2, 3))
output = torch.igammac(input, other)
print(output)