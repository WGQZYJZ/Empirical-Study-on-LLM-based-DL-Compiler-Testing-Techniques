'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.addmm_\ntorch.Tensor.addmm_(_input_tensor, mat1, mat2, *, beta=1, alpha=1)\n'
import torch
import torch
input_tensor = torch.randn(1, 1, 3, 3)
mat1 = torch.randn(1, 1, 3, 3)
mat2 = torch.randn(1, 1, 3, 3)
output_tensor = torch.Tensor.addmm_(input_tensor, mat1, mat2, beta=1, alpha=1)
print(output_tensor)
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.addmv_\ntorch.Tensor.addmv_(tensor, mat, vec, *, beta=1, alpha=1)\n'
import torch
import torch
input_tensor = torch.randn(1, 1, 3, 3)
mat = torch.rand