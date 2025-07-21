'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.rot90\ntorch.Tensor.rot90(_input_tensor, k, dims)\n'
import torch
input_tensor = torch.randn(2, 3, 4, 5)
print('Input tensor:', input_tensor)
k = 2
dims = [2, 3]
output_tensor = input_tensor.rot90(k, dims)
print('Output tensor:', output_tensor)