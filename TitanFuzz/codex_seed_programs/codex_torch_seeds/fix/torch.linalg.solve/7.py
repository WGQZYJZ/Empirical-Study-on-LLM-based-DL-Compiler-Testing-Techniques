'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.linalg.solve\ntorch.linalg.solve(A, B, *, out=None)\n'
import torch
A = torch.tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]], dtype=torch.float)
B = torch.tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]], dtype=torch.float)
X = torch.linalg.solve(A, B)
print(X)
'\nTask 1: Generate input data\nTask 2: Call the API torch.linalg.solve\ntorch.linalg.solve(A, B, *, out=None)\n'
A = torch.tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]], dtype=torch.float)
B = torch.tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]], dtype=torch.float)
X = torch.linalg.solve(A, B)
print(X)