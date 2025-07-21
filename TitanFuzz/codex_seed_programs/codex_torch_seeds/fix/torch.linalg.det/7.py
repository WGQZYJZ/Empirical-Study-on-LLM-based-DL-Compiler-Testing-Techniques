'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.linalg.det\ntorch.linalg.det(A, *, out=None)\n'
import torch
A = torch.rand((2, 2))
print(A)
print(torch.linalg.det(A))
'\nTask 4: Call the API torch.linalg.slogdet\ntorch.linalg.slogdet(A, *, out=None)\n'
print(torch.linalg.slogdet(A))
'\nTask 5: Call the API torch.linalg.solve\ntorch.linalg.solve(A, b)\n'
b = torch.rand((2, 2))
print(b)
print(torch.linalg.solve(A, b))
'\nTask 6: Call the API torch.linalg.svd\ntorch.linalg.svd(A, *, some=True, compute_uv=True)\n'
print(torch.linalg.svd(A))