'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.linalg.matrix_power\ntorch.linalg.matrix_power(A, n, *, out=None)\n'
import torch
from torch.autograd import Variable
import torch
A = Variable(torch.Tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
torch.linalg.matrix_power(A, 2)
torch.linalg.matrix_power(A, 3)