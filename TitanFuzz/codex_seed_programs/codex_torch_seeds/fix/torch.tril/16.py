'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.tril\ntorch.tril(input, diagonal=0, *, out=None)\n'
import torch
input_tensor = torch.randn(3, 3)
print('Input:')
print(input_tensor)
lower_triangular_tensor = torch.tril(input_tensor)
print('Lower triangular:')
print(lower_triangular_tensor)