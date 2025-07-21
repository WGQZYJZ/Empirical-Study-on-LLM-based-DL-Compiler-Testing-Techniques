'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.subtract_\ntorch.Tensor.subtract_(_input_tensor, other, *, alpha=1)\n'
import torch
input_tensor = torch.randint(0, 10, (3, 3), dtype=torch.float32)
other = torch.randint(0, 10, (3, 3), dtype=torch.float32)
output_tensor = input_tensor.subtract_(other)
print('input_tensor:', input_tensor)
print('other:', other)
print('output_tensor:', output_tensor)