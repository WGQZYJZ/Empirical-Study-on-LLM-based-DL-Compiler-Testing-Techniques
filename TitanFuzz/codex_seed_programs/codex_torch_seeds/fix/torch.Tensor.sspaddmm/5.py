'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.sspaddmm\ntorch.Tensor.sspaddmm(_input_tensor, mat1, mat2, *, beta=1, alpha=1)\n'
import torch
mat1 = torch.randn(4, 4)
mat2 = torch.randn(4, 4)
result = torch.Tensor.sspaddmm(mat1, mat2, mat1, beta=1, alpha=1)
print(result)