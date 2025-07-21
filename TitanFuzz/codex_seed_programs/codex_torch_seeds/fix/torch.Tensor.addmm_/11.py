'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.addmm_\ntorch.Tensor.addmm_(_input_tensor, mat1, mat2, *, beta=1, alpha=1)\n'
import torch
mat1 = torch.randn(2, 3)
mat2 = torch.randn(3, 4)
torch.Tensor.addmm_(mat1, mat1, mat2)
print(mat1)