'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.triangular_solve\ntorch.Tensor.triangular_solve(_input_tensor, A, upper=True, transpose=False, unitriangular=False)\n'
import torch
A = torch.randn(3, 3)
b = torch.randn(3)
x = torch.Tensor.triangular_solve(b, A, upper=True, transpose=False, unitriangular=False)
print(x)