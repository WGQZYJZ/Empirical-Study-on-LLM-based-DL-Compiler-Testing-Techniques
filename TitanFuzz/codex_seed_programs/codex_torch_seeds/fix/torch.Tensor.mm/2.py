'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.mm\ntorch.Tensor.mm(_input_tensor, mat2)\n'
import torch
mat1 = torch.tensor([[1, 2, 3], [4, 5, 6]], dtype=torch.float32)
mat2 = torch.tensor([[1, 2], [3, 4], [5, 6]], dtype=torch.float32)
result = torch.Tensor.mm(mat1, mat2)
print(result)