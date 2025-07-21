'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.tril\ntorch.tril(input, diagonal=0, *, out=None)\n'
import torch
input_data = torch.randn(4, 4)
print('input_data: ', input_data)
result = torch.tril(input_data, diagonal=1)
print('Result: ', result)
result = torch.tril(input_data, diagonal=0)
print('Result: ', result)
result = torch.tril(input_data, diagonal=2)
print('Result: ', result)