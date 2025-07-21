'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.sparse_dim\ntorch.Tensor.sparse_dim(_input_tensor)\n'
import torch
input_tensor = torch.randn(3, 3)
print('Input tensor: ', input_tensor)
print('Output tensor: ', input_tensor.sparse_dim())