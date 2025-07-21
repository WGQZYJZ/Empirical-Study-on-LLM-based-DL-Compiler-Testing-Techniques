'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.to_sparse\ntorch.Tensor.to_sparse(_input_tensor, sparseDims)\n'
import torch
input_tensor = torch.randn(2, 2, 3)
sparse_tensor = input_tensor.to_sparse()
print('input_tensor: ', input_tensor)
print('sparse_tensor: ', sparse_tensor)