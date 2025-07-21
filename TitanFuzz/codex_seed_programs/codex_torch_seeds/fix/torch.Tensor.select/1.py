'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.select\ntorch.Tensor.select(_input_tensor, dim, index)\n'
import torch
import torch
input_tensor = torch.rand(5, 3)
print('Input tensor:')
print(input_tensor)
output_tensor = torch.Tensor.select(input_tensor, dim=1, index=2)
print('Output tensor:')
print(output_tensor)