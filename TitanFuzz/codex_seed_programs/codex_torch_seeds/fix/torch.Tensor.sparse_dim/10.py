'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.sparse_dim\ntorch.Tensor.sparse_dim(_input_tensor)\n'
import torch
input_tensor = torch.randn(1, 4, 5, 6)
output = torch.Tensor.sparse_dim(input_tensor)
print(output)