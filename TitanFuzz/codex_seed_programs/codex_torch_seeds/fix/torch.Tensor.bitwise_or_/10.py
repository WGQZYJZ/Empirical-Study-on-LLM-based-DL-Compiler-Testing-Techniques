'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.bitwise_or_\ntorch.Tensor.bitwise_or_(_input_tensor, other)\n'
import torch
import numpy as np
input_tensor = torch.randint(low=0, high=2, size=(5, 5), dtype=torch.uint8)
other = torch.randint(low=0, high=2, size=(5, 5), dtype=torch.uint8)
output_tensor = input_tensor.bitwise_or_(other)
print('input_tensor: ', input_tensor)
print('other: ', other)
print('output_tensor: ', output_tensor)