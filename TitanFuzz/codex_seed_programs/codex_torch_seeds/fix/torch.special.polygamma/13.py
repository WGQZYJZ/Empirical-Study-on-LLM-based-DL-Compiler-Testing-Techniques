'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.special.polygamma\ntorch.special.polygamma(n, input, *, out=None)\n'
import torch
input_tensor = torch.randn(2, 3)
print('Input data: ', input_tensor)
result = torch.special.polygamma(1, input_tensor)
print('Result: ', result)