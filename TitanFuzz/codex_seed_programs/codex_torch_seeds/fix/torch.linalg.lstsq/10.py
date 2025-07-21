'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.linalg.lstsq\ntorch.linalg.lstsq(A, B, rcond=None, *, driver=None)\n'
import torch
A = torch.randn(2, 3)
B = torch.randn(2, 1)
X = torch.linalg.lstsq(A, B)
print(X)
'\nTask 4: Call the API torch.linalg.solve\ntorch.linalg.solve(A, B, *, rcond=None, upper=True, transpose=False, unitriangular=False, driver=None)\n'
A = torch.randn(2, 2)
B = torch.randn(2, 1)
X = torch.linalg.solve(A, B)
print(X)
'\nTask 5: Call the API torch.linalg.svd\ntorch.linalg.svd(A, *, some=False, compute_uv=True, out=None)\n'
A = torch.randn(2, 3)
(U, S, V) = torch.linalg.svd(A)
print(U)
print(S)
print(V)