'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.index_fill\ntorch.Tensor.index_fill(_input_tensor, dim, index, value)\n'
import torch
'\nTask 1: import PyTorch\n'
'\nTask 2: Generate input data\n'
input_tensor = torch.randn(3, 3)
print('input_tensor:', input_tensor)
'\nTask 3: Call the API torch.Tensor.index_fill\ntorch.Tensor.index_fill(_input_tensor, dim, index, value)\n'
index_tensor = torch.tensor([0, 2])
output_tensor = input_tensor.index_fill(0, index_tensor, (- 1))
print('output_tensor:', output_tensor)