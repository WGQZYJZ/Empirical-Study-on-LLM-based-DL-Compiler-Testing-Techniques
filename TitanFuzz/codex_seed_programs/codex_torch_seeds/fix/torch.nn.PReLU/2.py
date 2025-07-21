'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.PReLU\ntorch.nn.PReLU(num_parameters=1, init=0.25, device=None, dtype=None)\n'
import torch
input_data = torch.arange((- 5), 5, 0.1)
input_data = input_data.view(input_data.size(0), 1)
prelu = torch.nn.PReLU(num_parameters=1, init=0.25)
output = prelu(input_data)
print('input_data:', input_data)
print('output:', output)