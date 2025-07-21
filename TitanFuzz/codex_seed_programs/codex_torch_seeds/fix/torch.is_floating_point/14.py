'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.is_floating_point\ntorch.is_floating_point(input)\n'
import torch
input = torch.tensor([1, 2, 3, 4, 5], dtype=torch.float64)
print(torch.is_floating_point(input))