'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.addmv\ntorch.addmv(input, mat, vec, *, beta=1, alpha=1, out=None)\n'
import torch
A = torch.randn(4, 3)
x = torch.randn(3)
b = torch.randn(4)
out = torch.addmv(b, A, x)
print(out)
out = torch.addmv(b, A, x, alpha=0.5)
print(out)
out = torch.addmv(b, A, x, alpha=0.5, beta=2)
print(out)
out = torch.addmv(b, A, x, alpha=0.5, beta=2, out=b)
print(out)