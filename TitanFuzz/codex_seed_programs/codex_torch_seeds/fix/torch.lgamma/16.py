'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.lgamma\ntorch.lgamma(input, *, out=None)\n'
import torch
input_data = torch.tensor([1.0, 2.0, 3.0, 4.0])
output = torch.lgamma(input_data)
print(output)