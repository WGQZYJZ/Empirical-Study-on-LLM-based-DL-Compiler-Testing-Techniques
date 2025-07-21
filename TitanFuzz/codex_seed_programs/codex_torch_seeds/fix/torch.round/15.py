'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.round\ntorch.round(input, *, out=None)\n'
import torch
input_data = torch.FloatTensor([1.2, 2.3, 3.4, 4.5, 5.6, 6.7])
print('Input data: ', input_data)
output = torch.round(input_data)
print('Output: ', output)