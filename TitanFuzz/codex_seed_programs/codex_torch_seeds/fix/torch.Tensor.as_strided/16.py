'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.as_strided\ntorch.Tensor.as_strided(_input_tensor, size, stride, storage_offset=0)\n'
import torch
import torch
input_tensor = torch.arange(1, 16).view(3, 5)
print('input_tensor: {}'.format(input_tensor))
output_tensor = input_tensor.as_strided((3, 2), (5, 1))
print('output_tensor: {}'.format(output_tensor))