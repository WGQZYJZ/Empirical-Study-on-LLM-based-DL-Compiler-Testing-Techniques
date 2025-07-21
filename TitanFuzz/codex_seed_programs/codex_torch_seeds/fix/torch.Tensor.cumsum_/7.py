'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.cumsum_\ntorch.Tensor.cumsum_(_input_tensor, dim, dtype=None)\n'
import torch
input_tensor = torch.randint(low=0, high=10, size=(3, 3), dtype=torch.int32)
print('input_tensor:', input_tensor)
output_tensor = input_tensor.cumsum_(dim=1, dtype=torch.int32)
print('output_tensor:', output_tensor)