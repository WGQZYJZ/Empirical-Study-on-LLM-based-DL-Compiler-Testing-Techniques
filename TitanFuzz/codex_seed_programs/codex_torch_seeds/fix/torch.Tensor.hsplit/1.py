'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.hsplit\ntorch.Tensor.hsplit(_input_tensor, split_size_or_sections)\n'
import torch
input_tensor = torch.rand(2, 3, 4)
print(input_tensor)
print(torch.Tensor.hsplit(input_tensor, 2))