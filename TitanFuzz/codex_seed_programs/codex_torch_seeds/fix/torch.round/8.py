'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.round\ntorch.round(input, *, out=None)\n'
import torch
input_data = torch.tensor([0.9, 1.4, 2.6, 3.5, 4.6, 5.9, 6.9, 7.5, 8.9, 9.5])
print('The input data is: ', input_data)
output = torch.round(input_data)
print('The output is: ', output)
output = torch.round(input_data, out=None)
print('The output is: ', output)