'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.masked_select\ntorch.masked_select(input, mask, *, out=None)\n'
import torch
input_data = torch.randn(2, 3)
mask = input_data.ge(0.5)
print(torch.masked_select(input_data, mask))