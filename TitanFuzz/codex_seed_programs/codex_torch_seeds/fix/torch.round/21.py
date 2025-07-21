'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.round\ntorch.round(input, *, out=None)\n'
import torch
input_data = torch.tensor([1.5, 2.5, 3.5, 4.5])
output = torch.round(input_data)
print('Output: ', output)