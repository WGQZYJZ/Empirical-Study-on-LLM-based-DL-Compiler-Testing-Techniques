'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.cumprod\ntorch.cumprod(input, dim, *, dtype=None, out=None)\n'
import torch
input_data = torch.rand(2, 3)
print(input_data)
torch.cumprod(input_data, dim=1)