'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.cholesky_solve\ntorch.cholesky_solve(input, input2, upper=False, *, out=None)\n'
import torch
A = torch.tensor([[4.0, (- 2.0), 1.0], [(- 2.0), 4.0, (- 2.0)], [1.0, (- 2.0), 4.0]])
b = torch.tensor([[1.0], [4.0], [2.0]])
x = torch.cholesky_solve(b, A)
print(x)