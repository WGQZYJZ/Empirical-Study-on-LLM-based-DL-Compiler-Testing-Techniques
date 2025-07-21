'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.logical_or_\ntorch.Tensor.logical_or_(_input_tensor, other)\n'
import torch
input_tensor = torch.randint(0, 2, (4, 4), dtype=torch.bool)
other_tensor = torch.randint(0, 2, (4, 4), dtype=torch.bool)
out_tensor = input_tensor.logical_or_(other_tensor)
print('input_tensor:', input_tensor)
print('other_tensor:', other_tensor)
print('out_tensor:', out_tensor)