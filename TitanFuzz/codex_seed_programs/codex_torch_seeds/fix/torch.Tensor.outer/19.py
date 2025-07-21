'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.outer\ntorch.Tensor.outer(_input_tensor, vec2)\n'
import torch
input_tensor = torch.randn(4, 3)
vec2 = torch.randn(3)
print(torch.Tensor.outer(input_tensor, vec2))
'\nTask 4: Call the API torch.ger\ntorch.ger(vec1, vec2)\n'
vec1 = torch.randn(4)
vec2 = torch.randn(3)
print(torch.ger(vec1, vec2))
'\nTask 5: Call the API torch.matmul\ntorch.matmul(mat1, mat2)\n'
mat1 = torch.randn(4, 3)
mat2 = torch.randn(3, 5)
print(torch.matmul(mat1, mat2))