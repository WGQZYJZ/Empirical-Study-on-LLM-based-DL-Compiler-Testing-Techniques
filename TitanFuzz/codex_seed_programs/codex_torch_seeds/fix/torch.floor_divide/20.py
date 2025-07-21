'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.floor_divide\ntorch.floor_divide(input, other, *, out=None)\n'
import torch
input_tensor = torch.arange(1, 10, dtype=torch.float32)
print('Input Tensor: ', input_tensor)
result = torch.floor_divide(input_tensor, 2)
print('Result: ', result)