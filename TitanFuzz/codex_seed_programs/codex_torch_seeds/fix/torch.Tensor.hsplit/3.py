'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.hsplit\ntorch.Tensor.hsplit(_input_tensor, split_size_or_sections)\n'
import torch
input_tensor = torch.arange(0, 24)
input_tensor = input_tensor.view(4, 6)
print('input_tensor:')
print(input_tensor)
split_tensor = input_tensor.hsplit(2)
print('split_tensor:')
print(split_tensor)
split_tensor = input_tensor.hsplit([3, 4])
print('split_tensor:')
print(split_tensor)