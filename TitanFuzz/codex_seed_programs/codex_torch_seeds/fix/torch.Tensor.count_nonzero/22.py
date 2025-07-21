'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.count_nonzero\ntorch.Tensor.count_nonzero(_input_tensor, dim=None)\n'
import torch
input_tensor = torch.randn(2, 3)
print('Input tensor: ', input_tensor)
print('Number of non-zero elements in input tensor: ', input_tensor.count_nonzero())
print('Number of non-zero elements along dimension 0: ', input_tensor.count_nonzero(dim=0))
print('Number of non-zero elements along dimension 1: ', input_tensor.count_nonzero(dim=1))