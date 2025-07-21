'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.hsplit\ntorch.Tensor.hsplit(_input_tensor, split_size_or_sections)\n'
import torch
input_tensor = torch.randn(4, 4)
print(input_tensor)
split_size = 2
split_tensor = torch.Tensor.hsplit(input_tensor, split_size)
print(split_tensor)