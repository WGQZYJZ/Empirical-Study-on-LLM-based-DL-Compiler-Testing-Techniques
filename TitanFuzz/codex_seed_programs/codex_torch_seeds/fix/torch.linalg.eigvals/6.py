'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.linalg.eigvals\ntorch.linalg.eigvals(A, *, out=None)\n'
import torch
from torch.autograd import Variable
A = Variable(torch.Tensor([[1, 2], [3, 4]]), requires_grad=False)
eigvals = torch.linalg.eigvals(A)
print('eigvals =', eigvals)