'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.LocalResponseNorm\ntorch.nn.LocalResponseNorm(size, alpha=0.0001, beta=0.75, k=1.0)\n'
import torch
from torch.autograd import Variable
import torch
input = Variable(torch.randn(1, 3, 3, 3))
norm = torch.nn.LocalResponseNorm(3, alpha=0.0001, beta=0.75, k=1.0)
output = norm(input)
print('input: ', input)
print('output: ', output)