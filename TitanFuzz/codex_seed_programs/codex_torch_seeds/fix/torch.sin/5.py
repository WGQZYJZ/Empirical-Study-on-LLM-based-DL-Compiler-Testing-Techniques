'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.sin\ntorch.sin(input, *, out=None)\n'
import torch
data = torch.randn(1, 1, dtype=torch.float)
print(data)
sin_data = torch.sin(data)
print(sin_data)