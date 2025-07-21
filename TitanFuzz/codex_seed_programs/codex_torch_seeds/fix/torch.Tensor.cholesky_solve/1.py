'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.cholesky_solve\ntorch.Tensor.cholesky_solve(_input_tensor, input2, upper=False)\n'
import torch
input_tensor = torch.randn(3, 3)
input_tensor = input_tensor.mm(input_tensor.t())
input2 = torch.randn(3, 2)
cholesky_solve = torch.Tensor.cholesky_solve(input_tensor, input2, upper=False)
print(cholesky_solve)