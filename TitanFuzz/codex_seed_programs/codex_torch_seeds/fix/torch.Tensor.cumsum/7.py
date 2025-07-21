'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.cumsum\ntorch.Tensor.cumsum(_input_tensor, dim, dtype=None)\n'
import torch
input_tensor = torch.Tensor([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print('input_tensor: ', input_tensor)
output_tensor = input_tensor.cumsum(dim=1)
print('output_tensor: ', output_tensor)