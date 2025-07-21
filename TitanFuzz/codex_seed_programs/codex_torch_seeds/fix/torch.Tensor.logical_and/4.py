'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.logical_and\ntorch.Tensor.logical_and(_input_tensor, other)\n'
import torch
input_tensor = torch.randint(low=0, high=2, size=(4, 4), dtype=torch.int8)
other = torch.randint(low=0, high=2, size=(4, 4), dtype=torch.int8)
print(torch.Tensor.logical_and(input_tensor, other))