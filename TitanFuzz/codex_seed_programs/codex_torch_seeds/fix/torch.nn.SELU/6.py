'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.SELU\ntorch.nn.SELU(inplace=False)\n'
import torch
input_data = torch.tensor([[(- 1.0), 1.0], [1.0, (- 1.0)]])
selu = torch.nn.SELU(inplace=False)
output = selu(input_data)
print('input_data = ', input_data)
print('output = ', output)