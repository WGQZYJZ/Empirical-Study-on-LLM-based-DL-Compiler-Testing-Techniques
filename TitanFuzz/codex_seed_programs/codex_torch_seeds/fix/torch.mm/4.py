'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.mm\ntorch.mm(input, mat2, *, out=None)\n'
import torch
mat1 = torch.tensor([[1, 2, 3], [4, 5, 6]])
mat2 = torch.tensor([[1, 2], [3, 4], [5, 6]])
result = torch.mm(mat1, mat2)
print(result)
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.matmul\ntorch.matmul(input, other, *, out=None)\n'
import torch
mat1 = torch.tensor([[1, 2, 3], [4, 5, 6]])
mat2 = torch.tensor([[1, 2], [3, 4], [5, 6]])
result = torch.matmul(mat1, mat2)
print(result)