'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.sspaddmm\ntorch.Tensor.sspaddmm(_input_tensor, mat1, mat2, *, beta=1, alpha=1)\n'
import torch
input_tensor = torch.rand(4, 4)
mat1 = torch.rand(4, 4)
mat2 = torch.rand(4, 4)
print('Input Tensor: ', input_tensor)
print('Matrix 1: ', mat1)
print('Matrix 2: ', mat2)
result = torch.Tensor.sspaddmm(input_tensor, mat1, mat2)
print('Result: ', result)