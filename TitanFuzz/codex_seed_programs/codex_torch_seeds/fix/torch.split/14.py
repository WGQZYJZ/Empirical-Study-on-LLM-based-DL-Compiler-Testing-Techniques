'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.split\ntorch.split(tensor, split_size_or_sections, dim=0)\n'
import torch
input_tensor = torch.tensor([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(input_tensor)
print(torch.split(input_tensor, 2, dim=1))
print(torch.split(input_tensor, [1, 3, 1], dim=1))