'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.eq\ntorch.Tensor.eq(_input_tensor, other)\n'
import torch
input_tensor = torch.arange(start=1, end=6, dtype=torch.float32)
output_tensor = input_tensor.eq(3)
print('input_tensor:', input_tensor)
print('output_tensor:', output_tensor)