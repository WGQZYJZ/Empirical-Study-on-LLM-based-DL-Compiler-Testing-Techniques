'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.special.ndtri\ntorch.special.ndtri(input, *, out=None)\n'
import torch
input_data = torch.randn(2, 3)
print('Input data: ', input_data)
result = torch.special.ndtri(input_data)
print('Result: ', result)