'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.hsplit\ntorch.hsplit(input, indices_or_sections)\n'
import torch
data = torch.arange(0, 24).view(4, 6)
print(data)
print(torch.hsplit(data, 2))