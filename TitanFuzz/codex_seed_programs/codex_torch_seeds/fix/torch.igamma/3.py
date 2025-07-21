'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.igamma\ntorch.igamma(input, other, *, out=None)\n'
import torch
from torch.autograd import Variable
x = Variable(torch.randn(5, 5))
y = Variable(torch.randn(5, 5))
z = torch.igamma(x, y)
print(z)