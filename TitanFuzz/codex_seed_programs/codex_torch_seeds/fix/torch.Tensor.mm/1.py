'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.mm\ntorch.Tensor.mm(_input_tensor, mat2)\n'
import torch
mat1 = torch.Tensor([[1, 2], [3, 4]])
mat2 = torch.Tensor([[1, 1], [1, 1]])
output_tensor = torch.Tensor.mm(mat1, mat2)
print(output_tensor)