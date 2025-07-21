'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.sparse_dim\ntorch.Tensor.sparse_dim(_input_tensor)\n'
import torch
input_tensor = torch.randn(2, 3, 4, 5)
output_tensor = torch.Tensor.sparse_dim(input_tensor)
print('input_tensor:', input_tensor)
print('output_tensor:', output_tensor)