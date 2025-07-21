'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.to_sparse\ntorch.Tensor.to_sparse(_input_tensor, sparseDims)\n'
import torch
import torch
input_tensor = torch.randn(3, 4)
print('Input Tensor:')
print(input_tensor)
output_tensor = torch.Tensor.to_sparse(input_tensor, sparse_dim=1)
print('Output Tensor:')
print(output_tensor)