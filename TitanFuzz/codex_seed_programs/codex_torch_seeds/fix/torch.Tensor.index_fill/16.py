'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.index_fill\ntorch.Tensor.index_fill(_input_tensor, dim, index, value)\n'
import torch
import torch
input_tensor = torch.randn(2, 3)
print('input_tensor: ', input_tensor)
output_tensor = torch.Tensor.index_fill(input_tensor, 1, torch.tensor([0, 2]), 0)
print('output_tensor: ', output_tensor)