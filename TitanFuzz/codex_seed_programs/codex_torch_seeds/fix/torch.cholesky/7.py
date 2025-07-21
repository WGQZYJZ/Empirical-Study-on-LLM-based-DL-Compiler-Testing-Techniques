'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.cholesky\ntorch.cholesky(input, upper=False, *, out=None)\n'
import torch
input = torch.tensor([[4.0, 1.0, 1.0], [1.0, 2.0, 1.0], [1.0, 1.0, 2.0]])
output = torch.cholesky(input)
print(output)
y = torch.randn(3, 2)
x = torch.cholesky_solve(y, output)
print(x)
output_inverse = torch.cholesky_inverse(output)
print(output_inverse)
output_inverse_solve = torch.cholesky_inverse(output, upper=True)
print(output_inverse_solve)