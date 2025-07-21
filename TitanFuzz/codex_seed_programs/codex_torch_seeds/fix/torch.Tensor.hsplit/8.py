'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.hsplit\ntorch.Tensor.hsplit(_input_tensor, split_size_or_sections)\n'
import torch
print('Task 1: import PyTorch')
print(('-' * 40))
print('Task 2: Generate input data')
print(('-' * 40))
input_tensor = torch.arange(0, 12)
print('input_tensor = torch.arange(0, 12)')
print('input_tensor = \n{}'.format(input_tensor))
print('Task 3: Call the API torch.Tensor.hsplit')
print(('-' * 40))
print('torch.Tensor.hsplit(_input_tensor, split_size_or_sections)')
print(('-' * 40))
split_size = 2
split_tensors = input_tensor.hsplit(split_size)
print('split_size = 2')
print('split_tensors = input_tensor.hsplit(split_size)')
print('split_tensors = \n{}'.format(split_tensors))
split_size = 3