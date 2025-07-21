'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.sspaddmm\ntorch.Tensor.sspaddmm(_input_tensor, mat1, mat2, *, beta=1, alpha=1)\n'
import torch
import torch
input_tensor = torch.randn(2, 3, 4)
mat1 = torch.randn(4, 2)
mat2 = torch.randn(4, 3)
torch.Tensor.sspaddmm(input_tensor, mat1, mat2)