'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.triangular_solve\ntorch.Tensor.triangular_solve(_input_tensor, A, upper=True, transpose=False, unitriangular=False)\n'
import torch
A = torch.Tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
b = torch.Tensor([1, 2, 3])
x = torch.Tensor.triangular_solve(b, A, upper=True)
print(x)