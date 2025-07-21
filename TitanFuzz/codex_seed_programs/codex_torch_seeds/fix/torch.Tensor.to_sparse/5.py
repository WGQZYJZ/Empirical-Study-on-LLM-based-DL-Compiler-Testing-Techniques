'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.to_sparse\ntorch.Tensor.to_sparse(_input_tensor, sparseDims)\n'
import torch
input_tensor = torch.randn(3, 3, requires_grad=True)
print(input_tensor)
sparse_tensor = input_tensor.to_sparse()
print(sparse_tensor)
sparse_tensor = input_tensor.to_sparse(sparse_dim=0)
print(sparse_tensor)
sparse_tensor = input_tensor.to_sparse(sparse_dim=1)
print(sparse_tensor)
sparse_tensor = input_tensor.to_sparse(sparse_dim=2)
print(sparse_tensor)