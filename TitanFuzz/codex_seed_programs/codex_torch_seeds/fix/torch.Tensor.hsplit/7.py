'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.hsplit\ntorch.Tensor.hsplit(_input_tensor, split_size_or_sections)\n'
import torch
input_tensor = torch.rand(2, 4)
print('input_tensor = \n{}'.format(input_tensor))
split_size_or_sections = 2
output_tensor = torch.Tensor.hsplit(input_tensor, split_size_or_sections)
print('output_tensor = \n{}'.format(output_tensor))
split_size_or_sections = [2, 2]
output_tensor = torch.Tensor.hsplit(input_tensor, split_size_or_sections)
print('output_tensor = \n{}'.format(output_tensor))