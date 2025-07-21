"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.linalg.eigh\ntorch.linalg.eigh(A, UPLO='L', *, out=None)\n"
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from torch.autograd import Variable
print('Task 1: import PyTorch')
print('PyTorch version: ', torch.__version__)
print('Task 2: Generate input data')
A = torch.randn(2, 2)
print('A: ', A)
print('Task 3: Call the API torch.linalg.eigh')
(eigvals, eigvecs) = torch.linalg.eigh(A)
print('eigvals: ', eigvals)
print('eigvecs: ', eigvecs)
print('Task 4: Verify the result')