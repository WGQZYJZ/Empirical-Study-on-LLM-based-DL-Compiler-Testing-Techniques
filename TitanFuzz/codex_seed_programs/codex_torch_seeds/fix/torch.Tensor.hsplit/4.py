'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.hsplit\ntorch.Tensor.hsplit(_input_tensor, split_size_or_sections)\n'
import torch
input_tensor = torch.randn(2, 4)
split_tensor = input_tensor.hsplit(2)
print('The original tensor:', input_tensor)
print('The split tensor:', split_tensor)