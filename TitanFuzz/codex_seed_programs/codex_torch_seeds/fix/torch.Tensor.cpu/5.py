'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.cpu\ntorch.Tensor.cpu(_input_tensor, memory_format=torch.preserve_format)\n'
import torch
input_tensor = torch.randn(2, 3, 4, 5)
print('Input tensor: ', input_tensor)
output_tensor = torch.Tensor.cpu(input_tensor, memory_format=torch.preserve_format)
print('Output tensor: ', output_tensor)