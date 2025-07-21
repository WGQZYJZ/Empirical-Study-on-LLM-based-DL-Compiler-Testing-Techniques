'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.rot90\ntorch.Tensor.rot90(_input_tensor, k, dims)\n'
import torch
input_tensor = torch.randn(3, 3)
print('Input Tensor: ')
print(input_tensor)
output_tensor = torch.Tensor.rot90(input_tensor, 1, (0, 1))
print('Output Tensor: ')
print(output_tensor)