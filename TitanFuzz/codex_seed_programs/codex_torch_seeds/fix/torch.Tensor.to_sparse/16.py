'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.to_sparse\ntorch.Tensor.to_sparse(_input_tensor, sparseDims)\n'
import torch
import torch
input_tensor = torch.randn(3, 3)
output_tensor = torch.Tensor.to_sparse(input_tensor, sparse_dims=1)
print(output_tensor)