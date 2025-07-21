'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.cpu\ntorch.Tensor.cpu(_input_tensor, memory_format=torch.preserve_format)\n'
import torch
input_tensor = torch.randn(3, 3)
print('Input tensor: ', input_tensor)
output_tensor = input_tensor.cpu()
print('Output tensor: ', output_tensor)