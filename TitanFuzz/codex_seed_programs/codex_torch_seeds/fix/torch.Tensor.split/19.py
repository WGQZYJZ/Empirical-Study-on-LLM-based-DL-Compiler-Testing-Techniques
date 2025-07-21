'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.split\ntorch.Tensor.split(_input_tensor, split_size, dim=0)\n'
import torch
input_tensor = torch.rand(20, 10)
print('Input tensor:')
print(input_tensor)
output_tensor = input_tensor.split(split_size=5, dim=0)
print('Output tensor:')
print(output_tensor)