'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.addmm_\ntorch.Tensor.addmm_(_input_tensor, mat1, mat2, *, beta=1, alpha=1)\n'
import torch
mat1 = torch.randn(3, 4)
mat2 = torch.randn(4, 3)
torch.Tensor.addmm_(mat1, mat1, mat2, beta=1, alpha=1)
print(mat1)