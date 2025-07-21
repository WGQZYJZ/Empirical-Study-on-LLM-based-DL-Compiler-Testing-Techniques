'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.sspaddmm\ntorch.Tensor.sspaddmm(_input_tensor, mat1, mat2, *, beta=1, alpha=1)\n'
import torch
import torch
input_tensor = torch.rand(10, 10)
mat1 = torch.rand(10, 10)
mat2 = torch.rand(10, 10)
result = torch.Tensor.sspaddmm(input_tensor, mat1, mat2, beta=1, alpha=1)
print(result)