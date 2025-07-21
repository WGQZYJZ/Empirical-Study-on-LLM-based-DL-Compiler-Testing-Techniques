'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.sparse_dim\ntorch.Tensor.sparse_dim(_input_tensor)\n'
import torch
input_tensor = torch.rand((3, 3))
print('input_tensor: ', input_tensor)
torch.Tensor.sparse_dim(input_tensor)