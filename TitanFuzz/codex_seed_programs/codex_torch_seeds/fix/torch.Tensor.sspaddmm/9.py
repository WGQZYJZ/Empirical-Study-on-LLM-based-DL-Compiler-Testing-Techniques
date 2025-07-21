'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.sspaddmm\ntorch.Tensor.sspaddmm(_input_tensor, mat1, mat2, *, beta=1, alpha=1)\n'
import torch
_input_tensor = torch.rand(2, 3)
mat1 = torch.rand(3, 4)
mat2 = torch.rand(4, 5)
torch.Tensor.sspaddmm(_input_tensor, mat1, mat2, beta=1, alpha=1)