'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.isinf\ntorch.isinf(input)\n'
import torch
input_tensor = torch.randn(2, 3)
print('Input tensor: ', input_tensor)
result = torch.isinf(input_tensor)
print('Result: ', result)