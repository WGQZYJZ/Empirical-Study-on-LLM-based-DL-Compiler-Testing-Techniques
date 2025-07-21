'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.acosh\ntorch.acosh(input, *, out=None)\n'
import torch
input_tensor = torch.randn(2, 3)
print('Input data:')
print(input_tensor)
output_tensor = torch.acosh(input_tensor)
print('Output data:')
print(output_tensor)