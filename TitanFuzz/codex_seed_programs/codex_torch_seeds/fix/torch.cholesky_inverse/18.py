'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.cholesky_inverse\ntorch.cholesky_inverse(input, upper=False, *, out=None)\n'
import torch
from torch.autograd import Variable
input = Variable(torch.randn(3, 3), requires_grad=True)
print(input)
output = torch.cholesky_inverse(input)
print(output)