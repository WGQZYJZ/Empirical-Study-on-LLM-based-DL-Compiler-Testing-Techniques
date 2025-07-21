'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.hsplit\ntorch.Tensor.hsplit(_input_tensor, split_size_or_sections)\n'
import torch
input_tensor = torch.arange(0, 12).reshape(2, 6)
print('input_tensor:', input_tensor)
import torch
input_tensor = torch.arange(0, 12).reshape(2, 6)
print('input_tensor:', input_tensor)
split_tensor_list = input_tensor.hsplit(3)
print('split_tensor_list:', split_tensor_list)
print('split_tensor_list[0]:', split_tensor_list[0])
print('split_tensor_list[1]:', split_tensor_list[1])
print('split_tensor_list[2]:', split_tensor_list[2])