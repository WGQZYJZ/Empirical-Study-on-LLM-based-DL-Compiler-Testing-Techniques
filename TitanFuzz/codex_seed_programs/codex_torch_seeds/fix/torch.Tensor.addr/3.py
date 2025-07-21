'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.addr\ntorch.Tensor.addr(_input_tensor, vec1, vec2, *, beta=1, alpha=1)\n'
import torch
vec1 = torch.arange(1, 4)
vec2 = torch.arange(1, 3)
matrix = torch.tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(vec1.addr(vec2))
print(matrix.addr(vec1, vec2))