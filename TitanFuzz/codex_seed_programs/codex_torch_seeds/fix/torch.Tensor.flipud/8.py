'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.flipud\ntorch.Tensor.flipud(_input_tensor)\n'
import torch
input_tensor = torch.arange(0, 9).view(3, 3)
print('Original input tensor:')
print(input_tensor)
output_tensor = torch.Tensor.flipud(input_tensor)
print('\nOutput tensor:')
print(output_tensor)