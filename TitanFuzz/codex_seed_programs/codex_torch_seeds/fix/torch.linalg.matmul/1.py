'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.linalg.matmul\ntorch.linalg.matmul(input, other, *, out=None)\n'
import torch
a = torch.tensor([[1, 2, 3], [4, 5, 6]])
b = torch.tensor([[1, 2], [3, 4], [5, 6]])
print(torch.linalg.matmul(a, b))
print(torch.matmul(a, b))