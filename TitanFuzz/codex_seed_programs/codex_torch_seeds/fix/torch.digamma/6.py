'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.digamma\ntorch.digamma(input, *, out=None)\n'
import torch
input_data = torch.tensor([2.0, 3.0, 4.0])
output_data = torch.digamma(input_data)
print('Output data:\n', output_data)