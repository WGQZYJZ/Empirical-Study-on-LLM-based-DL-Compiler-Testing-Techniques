'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.rot90\ntorch.Tensor.rot90(_input_tensor, k, dims)\n'
import torch
'\nTask 1: Generate input data\n'
input_tensor = torch.randn(4, 4)
print('Input data:')
print(input_tensor)
'\nTask 2: Call the API torch.Tensor.rot90\ntorch.Tensor.rot90(_input_tensor, k, dims)\n'
output_tensor = input_tensor.rot90(1, (0, 1))
print('Output data:')
print(output_tensor)