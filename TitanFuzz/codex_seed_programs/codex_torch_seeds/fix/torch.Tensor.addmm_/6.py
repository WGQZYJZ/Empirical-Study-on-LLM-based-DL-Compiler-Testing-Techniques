'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.addmm_\ntorch.Tensor.addmm_(_input_tensor, mat1, mat2, *, beta=1, alpha=1)\n'
import torch
input_tensor = torch.rand(2, 3)
mat1 = torch.rand(2, 3)
mat2 = torch.rand(3, 3)
torch.Tensor.addmm_(input_tensor, mat1, mat2, beta=1, alpha=1)
print('input_tensor:', input_tensor)
print('mat1:', mat1)
print('mat2:', mat2)