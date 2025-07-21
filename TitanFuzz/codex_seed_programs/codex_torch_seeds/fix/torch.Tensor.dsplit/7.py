'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.dsplit\ntorch.Tensor.dsplit(_input_tensor, split_size_or_sections)\n'
import torch
input_tensor = torch.randn(4, 4)
print('Input Tensor:')
print(input_tensor)
splitted_tensor = input_tensor.dsplit(2)
print('\nSplitted Tensor:')
print(splitted_tensor)
print('\nSplitted Tensor size:')
print(len(splitted_tensor))