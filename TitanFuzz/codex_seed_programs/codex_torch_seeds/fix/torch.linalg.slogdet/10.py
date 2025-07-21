'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.linalg.slogdet\ntorch.linalg.slogdet(A, *, out=None)\n'
import torch
print(torch.__version__)
A = torch.randn(10, 10)
print(torch.linalg.slogdet(A))