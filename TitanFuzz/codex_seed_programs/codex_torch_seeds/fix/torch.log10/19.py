'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.log10\ntorch.log10(input, *, out=None)\n'
import torch
input_data = torch.tensor([1, 10, 100, 1000], dtype=torch.float)
log_10 = torch.log10(input_data)
print(log_10)