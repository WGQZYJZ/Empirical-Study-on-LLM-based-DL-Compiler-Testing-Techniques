'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.sqrt\ntorch.sqrt(input, *, out=None)\n'
import torch
data = torch.randn(2, 2)
print('Input Data: ', data)
print('Output Data: ', torch.sqrt(data))