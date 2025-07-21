'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.sparse_dim\ntorch.Tensor.sparse_dim(_input_tensor)\n'
import torch
input_tensor = torch.randn(3, 3, requires_grad=True)
sparse_dim = input_tensor.sparse_dim()
print('sparse_dim: ', sparse_dim)