'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.linalg.matrix_power\ntorch.linalg.matrix_power(A, n, *, out=None)\n'
import torch
from torch.autograd import Variable
import torch
A = Variable(torch.randn(3, 3))
n = 2
print(torch.linalg.matrix_power(A, n))