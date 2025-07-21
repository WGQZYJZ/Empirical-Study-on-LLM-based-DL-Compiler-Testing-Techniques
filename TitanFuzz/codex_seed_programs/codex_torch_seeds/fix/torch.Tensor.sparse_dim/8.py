'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.sparse_dim\ntorch.Tensor.sparse_dim(_input_tensor)\n'
import torch
input_tensor = torch.tensor([[1, 0, 0, 0], [0, 2, 0, 0], [0, 0, 3, 0], [0, 0, 0, 4]])
result = torch.Tensor.sparse_dim(input_tensor)
print(result)