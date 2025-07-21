'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.dsplit\ntorch.Tensor.dsplit(_input_tensor, split_size_or_sections)\n'
import torch
input_tensor = torch.randn(5, 2, 3)
print('input_tensor:', input_tensor)
output_tensors = input_tensor.dsplit(split_size=1)
print('output_tensors:', output_tensors)