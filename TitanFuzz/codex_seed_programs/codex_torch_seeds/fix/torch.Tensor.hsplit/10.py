'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.hsplit\ntorch.Tensor.hsplit(_input_tensor, split_size_or_sections)\n'
import torch
input_tensor = torch.randn(2, 4, 3)
print('input_tensor: ', input_tensor)
output_tensor = input_tensor.hsplit(2)
print('output_tensor: ', output_tensor)