'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.flip\ntorch.Tensor.flip(_input_tensor, dims)\n'
import torch
input_tensor = torch.arange(start=0, end=9, step=1).reshape(3, 3)
print('input_tensor: ')
print(input_tensor)
output_tensor = torch.Tensor.flip(input_tensor, dims=[0])
print('output_tensor: ')
print(output_tensor)