'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.to_sparse\ntorch.Tensor.to_sparse(_input_tensor, sparseDims)\n'
import torch
_input_tensor = torch.rand(2, 3, 4)
print('Input Tensor:', _input_tensor)
_sparse_tensor = _input_tensor.to_sparse(sparseDims=2)
print('Sparse Tensor:', _sparse_tensor)