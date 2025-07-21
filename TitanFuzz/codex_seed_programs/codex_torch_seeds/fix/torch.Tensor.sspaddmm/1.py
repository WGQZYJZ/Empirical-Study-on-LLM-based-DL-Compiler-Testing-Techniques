'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.sspaddmm\ntorch.Tensor.sspaddmm(_input_tensor, mat1, mat2, *, beta=1, alpha=1)\n'
import torch
input_tensor = torch.tensor([[1, 2, 3], [4, 5, 6]])
mat1 = torch.tensor([[1, 2], [3, 4], [5, 6]])
mat2 = torch.tensor([[1, 2, 3], [4, 5, 6]])
output_tensor = torch.Tensor.sspaddmm(input_tensor, mat1, mat2)
print('output_tensor = ', output_tensor)