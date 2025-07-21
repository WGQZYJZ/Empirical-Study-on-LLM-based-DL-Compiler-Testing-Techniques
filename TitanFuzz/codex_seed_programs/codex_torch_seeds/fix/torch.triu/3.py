'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.triu\ntorch.triu(input, diagonal=0, *, out=None)\n'
import torch
input_data = torch.rand(3, 3)
print('Input Data:')
print(input_data)
print('\nUpper triangular portion of the input:')
print(torch.triu(input_data))
print('\nUpper triangular portion of the input with diagonal = 1:')
print(torch.triu(input_data, diagonal=1))
print('\nUpper triangular portion of the input with diagonal = -1:')
print(torch.triu(input_data, diagonal=(- 1)))