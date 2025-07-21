'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.hsplit\ntorch.Tensor.hsplit(_input_tensor, split_size_or_sections)\n'
import torch
input_tensor = torch.rand(10, 3)
output_tensors = input_tensor.hsplit(3)
print('input_tensor: ', input_tensor)
print('output_tensors: ', output_tensors)