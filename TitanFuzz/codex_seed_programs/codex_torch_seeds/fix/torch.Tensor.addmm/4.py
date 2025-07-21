'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.addmm\ntorch.Tensor.addmm(_input_tensor, mat1, mat2, *, beta=1, alpha=1)\n'
import torch
input_tensor = torch.randn(2, 3)
mat1 = torch.randn(3, 4)
mat2 = torch.randn(4, 3)
output_tensor = torch.Tensor.addmm(input_tensor, mat1, mat2, beta=1, alpha=1)
print(output_tensor)