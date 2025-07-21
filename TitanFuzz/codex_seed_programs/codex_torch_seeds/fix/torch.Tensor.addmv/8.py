'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.addmv\ntorch.Tensor.addmv(_input_tensor, mat, vec, *, beta=1, alpha=1)\n'
import torch
input_tensor = torch.rand(2, 3)
mat = torch.rand(3, 4)
vec = torch.rand(4)
output_tensor = torch.Tensor.addmv(input_tensor, mat, vec)
print(output_tensor)