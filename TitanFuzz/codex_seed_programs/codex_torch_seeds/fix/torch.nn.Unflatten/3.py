'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.Unflatten\ntorch.nn.Unflatten(dim, unflattened_size)\n'
import torch
input_data = torch.rand(1, 1, 4, 4)
print(input_data)
unflatten = torch.nn.Unflatten(2, (2, 2))
print(unflatten(input_data))