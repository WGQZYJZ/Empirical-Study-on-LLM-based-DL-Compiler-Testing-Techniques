'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.hsplit\ntorch.Tensor.hsplit(_input_tensor, split_size_or_sections)\n'
import torch
'\nTask 1: import PyTorch\n'
'\nTask 2: Generate input data\n'
input_tensor = torch.arange(0, 16, dtype=torch.float32).view(2, 8)
print('input_tensor:', input_tensor)
'\nTask 3: Call the API torch.Tensor.hsplit\ntorch.Tensor.hsplit(_input_tensor, split_size_or_sections)\n'
output_tensor_list = torch.Tensor.hsplit(input_tensor, split_size_or_sections=4)
print('output_tensor_list:', output_tensor_list)
for (i, tensor) in enumerate(output_tensor_list):
    print(('output_tensor_list[%d]:' % i), tensor)