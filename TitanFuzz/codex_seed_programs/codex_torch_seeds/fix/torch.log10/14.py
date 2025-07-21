'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.log10\ntorch.log10(input, *, out=None)\n'
import torch
input_data = torch.tensor([10, 100, 1000])
print(input_data)
print('\nThe output of torch.log10(input_data) is:')
print(torch.log10(input_data))