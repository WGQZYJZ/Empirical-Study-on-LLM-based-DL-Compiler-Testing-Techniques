'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.flip\ntorch.Tensor.flip(_input_tensor, dims)\n'
import torch
input_tensor = torch.randint(0, 10, (2, 3, 4))
print('Input tensor:')
print(input_tensor)
output_tensor = torch.Tensor.flip(input_tensor, dims=(0, 1))
print('Output tensor:')
print(output_tensor)