'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.logical_and\ntorch.Tensor.logical_and(_input_tensor, other)\n'
import torch
input_tensor = torch.randint(0, 2, (3, 3), dtype=torch.bool)
other = torch.randint(0, 2, (3, 3), dtype=torch.bool)
result = torch.Tensor.logical_and(input_tensor, other)
print(result)