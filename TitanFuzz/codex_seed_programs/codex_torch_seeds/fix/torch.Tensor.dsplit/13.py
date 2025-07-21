'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.dsplit\ntorch.Tensor.dsplit(_input_tensor, split_size_or_sections)\n'
import torch
import torch
input_tensor = torch.arange(start=0, end=24, dtype=torch.float32).reshape(2, 3, 4)
print('input_tensor: ', input_tensor)
split_tensor_list = torch.Tensor.dsplit(input_tensor, split_size_or_sections=2)
print('split_tensor_list: ', split_tensor_list)