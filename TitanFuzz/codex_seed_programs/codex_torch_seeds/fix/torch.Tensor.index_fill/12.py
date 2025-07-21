'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.index_fill\ntorch.Tensor.index_fill(_input_tensor, dim, index, value)\n'
import torch
input_tensor = torch.randn(2, 3)
print('input_tensor: {}'.format(input_tensor))
dim = 1
index = torch.tensor([0, 2])
value = 0
output_tensor = torch.Tensor.index_fill(input_tensor, dim, index, value)
print('output_tensor: {}'.format(output_tensor))