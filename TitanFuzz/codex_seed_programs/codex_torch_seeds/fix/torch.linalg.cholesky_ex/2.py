'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.linalg.cholesky_ex\ntorch.linalg.cholesky_ex(A, *, upper=False, check_errors=False, out=None)\n'
import torch
input_data = torch.randn(3, 3)
print(input_data)
import torch
input_data = torch.randn(3, 3)
print(input_data)
output = torch.linalg.cholesky_ex(input_data, upper=False, check_errors=False)
print(output)
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.linalg.cholesky_solve\ntorch.linalg.cholesky_solve(A, b, *, upper=False, check_errors=False, out=None)\n'
import torch
input_data = torch.randn(3, 3)
print(input_data)
import torch