'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.index_fill\ntorch.Tensor.index_fill(_input_tensor, dim, index, value)\n'
import torch
'\nTask 2: Generate input data\n'
input_tensor = torch.tensor([[1, 2, 3], [4, 5, 6]])
print('Input Tensor: ', input_tensor)
'\nTask 3: Call the API torch.Tensor.index_fill\ntorch.Tensor.index_fill(_input_tensor, dim, index, value)\n'
output_tensor = input_tensor.index_fill(0, torch.tensor([0]), 10)
print('Output Tensor: ', output_tensor)