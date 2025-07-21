'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.special.erfinv\ntorch.special.erfinv(input, *, out=None)\n'
import torch
input_data = torch.rand(1, 2, 3)
print(input_data)
print(torch.special.erfinv(input_data))