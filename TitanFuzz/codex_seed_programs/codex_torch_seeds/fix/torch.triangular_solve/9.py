'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.triangular_solve\ntorch.triangular_solve(b, A, upper=True, transpose=False, unitriangular=False)\n'
import torch
A = torch.tensor([[3, 0, 0], [1, 2, 0], [0, 1, 1]], dtype=torch.float)
b = torch.tensor([[2, 3, 3]], dtype=torch.float).t()
x = torch.triangular_solve(b, A, upper=True)[0]
print(x)