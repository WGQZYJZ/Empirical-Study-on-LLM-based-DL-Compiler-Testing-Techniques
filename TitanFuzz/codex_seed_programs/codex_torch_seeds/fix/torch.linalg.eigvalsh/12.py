"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.linalg.eigvalsh\ntorch.linalg.eigvalsh(A, UPLO='L', *, out=None)\n"
import torch
from torch.autograd import Variable
from torch.autograd import gradcheck
dtype = torch.float
device = torch.device('cpu')
N = 10
A = torch.randn(N, N, dtype=dtype, device=device)
A = A.mm(A.t())
eigvals = torch.linalg.eigvalsh(A)
print(eigvals)