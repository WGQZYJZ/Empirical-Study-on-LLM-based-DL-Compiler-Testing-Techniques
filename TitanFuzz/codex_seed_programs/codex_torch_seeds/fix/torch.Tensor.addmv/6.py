'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.addmv\ntorch.Tensor.addmv(_input_tensor, mat, vec, *, beta=1, alpha=1)\n'
import torch
input_tensor = torch.randn(1, 2, 3, 4)
mat = torch.randn(2, 3)
vec = torch.randn(3, 4)
output_tensor = input_tensor.addmv(mat, vec)
print(output_tensor)