'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.hsplit\ntorch.Tensor.hsplit(_input_tensor, split_size_or_sections)\n'
import torch
input_tensor = torch.randn(2, 6)
print(input_tensor)
split_size = 3
split_sections = [3, 3]
output_tensor_1 = input_tensor.hsplit(split_size)
output_tensor_2 = input_tensor.hsplit(split_sections)
print(output_tensor_1)
print(output_tensor_2)