'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.split\ntorch.split(tensor, split_size_or_sections, dim=0)\n'
import torch
input_data = torch.arange(0, 10)
print(torch.split(input_data, 2, dim=0))