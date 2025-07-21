'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.split\ntorch.split(tensor, split_size_or_sections, dim=0)\n'
import torch
tensor = torch.randn(2, 3, 4)
result = torch.split(tensor, split_size_or_sections=2, dim=0)
print(result)