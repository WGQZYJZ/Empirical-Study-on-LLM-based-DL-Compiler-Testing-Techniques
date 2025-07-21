'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.round\ntorch.round(input, *, out=None)\n'
import torch
input_data = torch.tensor([1.2, 2.3, 3.4, 4.5, 5.6, 6.7])
output = torch.round(input_data)
print('The input data is: ', input_data)
print('The rounded data is: ', output)