'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.ne\ntorch.ne(input, other, *, out=None)\n'
import torch
input_data = torch.randn(3)
print(input_data)
torch.ne(input_data, torch.zeros(3))