'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.msort\ntorch.msort(input, *, out=None)\n'
import torch
data = torch.rand(10, 3)
sorted_data = torch.msort(data)
print(sorted_data)