'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.linalg.matrix_power\ntorch.linalg.matrix_power(A, n, *, out=None)\n'
import torch
from torch.autograd import Variable
x = Variable(torch.randn(1, 3, 3))
print(torch.linalg.matrix_power(x, 2))