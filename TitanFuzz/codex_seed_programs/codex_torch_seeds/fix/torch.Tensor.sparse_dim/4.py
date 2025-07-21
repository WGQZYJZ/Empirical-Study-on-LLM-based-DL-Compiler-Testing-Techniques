'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.sparse_dim\ntorch.Tensor.sparse_dim(_input_tensor)\n'
import torch
input_tensor = torch.tensor([[1, 1, 0, 0], [0, 0, 1, 1]])
print('Input tensor: ', input_tensor)
print('Sparse dimension: ', input_tensor.sparse_dim())