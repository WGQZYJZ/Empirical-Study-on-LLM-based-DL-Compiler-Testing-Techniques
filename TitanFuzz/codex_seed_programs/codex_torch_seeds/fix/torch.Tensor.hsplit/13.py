'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.hsplit\ntorch.Tensor.hsplit(_input_tensor, split_size_or_sections)\n'
import torch
_input_tensor = torch.rand(5, 3)
print('Input tensor: ', _input_tensor)
_split_size_or_sections = 2
_splitted_tensor = torch.Tensor.hsplit(_input_tensor, _split_size_or_sections)
print('Splitted tensor: ', _splitted_tensor)
_split_size_or_sections = [2, 1]
_splitted_tensor = torch.Tensor.hsplit(_input_tensor, _split_size_or_sections)
print('Splitted tensor: ', _splitted_tensor)
_split_size_or_sections = [1, 2]
_splitted_tensor = torch.Tensor.hsplit(_input_tensor, _split_size_or_sections)
print('Splitted tensor: ', _splitted_tensor)
_split_size_or_sections = [(- 1), 1]