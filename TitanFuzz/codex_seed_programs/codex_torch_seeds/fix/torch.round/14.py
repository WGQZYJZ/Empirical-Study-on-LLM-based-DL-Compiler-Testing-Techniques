'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.round\ntorch.round(input, *, out=None)\n'
import torch
input_data = torch.tensor([1.3, 2.1, 3.9, 4.0, 5.9, 6.7])
print(input_data)
print(torch.round(input_data))