'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.addmm_\ntorch.Tensor.addmm_(_input_tensor, mat1, mat2, *, beta=1, alpha=1)\n'
import torch
mat1 = torch.Tensor([[1, 2, 3], [4, 5, 6]])
mat2 = torch.Tensor([[1, 2], [3, 4], [5, 6]])
result = torch.Tensor([[0, 0], [0, 0]])
result.addmm_(mat1, mat2)
print(result)