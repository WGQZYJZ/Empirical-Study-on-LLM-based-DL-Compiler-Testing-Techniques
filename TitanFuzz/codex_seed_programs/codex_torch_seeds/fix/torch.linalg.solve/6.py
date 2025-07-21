'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.linalg.solve\ntorch.linalg.solve(A, B, *, out=None)\n'
import torch
A = torch.tensor([[2.0, 1.0], [1.0, 3.0]])
B = torch.tensor([[1.0, 2.0], [3.0, 4.0]])
X = torch.linalg.solve(A, B)
print(X)
'\nTask 4: Verify the result\n'
print(torch.matmul(A, X))
print(B)