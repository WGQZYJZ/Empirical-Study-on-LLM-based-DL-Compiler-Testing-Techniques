'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.float\ntorch.Tensor.float(_input_tensor, memory_format=torch.preserve_format)\n'
import torch
input_data = torch.rand(2, 3)
print('input_data:', input_data)
output_data = torch.Tensor.float(input_data)
print('output_data:', output_data)