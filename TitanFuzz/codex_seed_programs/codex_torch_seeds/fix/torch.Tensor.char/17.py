'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.char\ntorch.Tensor.char(_input_tensor, memory_format=torch.preserve_format)\n'
import torch
input_tensor = torch.randn(3, 3)
print('Input tensor: {}'.format(input_tensor))
print('\nTask 1: import PyTorch')
print('\nTask 2: Generate input data')
print('\nTask 3: Call the API torch.Tensor.char')
char_tensor = input_tensor.char()
print('char_tensor: {}'.format(char_tensor))