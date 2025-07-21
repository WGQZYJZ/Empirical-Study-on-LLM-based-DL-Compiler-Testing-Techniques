"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.linalg.matrix_norm\ntorch.linalg.matrix_norm(A, ord='fro', dim=(-2, -1), keepdim=False, *, dtype=None, out=None)\n"
import torch
from torch.autograd import Variable
A = Variable(torch.randn(4, 4), requires_grad=True)
print('A: ', A)
B = torch.linalg.matrix_norm(A)
print('B: ', B)
B.backward()
print('A.grad: ', A.grad)