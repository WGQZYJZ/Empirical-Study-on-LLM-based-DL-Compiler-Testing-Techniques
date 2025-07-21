'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.sspaddmm\ntorch.Tensor.sspaddmm(_input_tensor, mat1, mat2, *, beta=1, alpha=1)\n'
import torch
input_tensor = torch.randn(4, 4)
mat1 = torch.randn(4, 4)
mat2 = torch.randn(4, 4)
print('Input tensor:', input_tensor)
print('mat1:', mat1)
print('mat2:', mat2)
output_tensor = torch.Tensor.sspaddmm(input_tensor, mat1, mat2, beta=1, alpha=1)
print('Output tensor:', output_tensor)