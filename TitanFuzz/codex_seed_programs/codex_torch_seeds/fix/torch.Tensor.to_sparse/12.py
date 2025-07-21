'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.to_sparse\ntorch.Tensor.to_sparse(_input_tensor, sparseDims)\n'
import torch
input_tensor = torch.randn(3, 3)
output_tensor = input_tensor.to_sparse(sparse_dim=1)
print('The input tensor is:', input_tensor)
print('The output tensor is:', output_tensor)