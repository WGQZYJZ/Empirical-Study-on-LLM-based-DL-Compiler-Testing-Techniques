'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.take_along_dim\ntorch.Tensor.take_along_dim(_input_tensor, indices, dim)\n'
import torch
input_tensor = torch.tensor([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
indices = torch.tensor([[0, 1, 2], [1, 2, 0], [0, 1, 2]])
dim = 1
result = torch.Tensor.take_along_dim(input_tensor, indices, dim)
print(result)