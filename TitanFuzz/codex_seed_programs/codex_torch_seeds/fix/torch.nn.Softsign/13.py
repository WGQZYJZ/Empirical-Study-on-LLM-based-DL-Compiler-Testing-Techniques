'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.Softsign\ntorch.nn.Softsign()\n'
import torch
import torch.nn as nn
input_data = torch.tensor([(- 1), (- 0.5), 0, 0.5, 1], dtype=torch.float)
softsign = nn.Softsign()
output = softsign(input_data)
print('input: ', input_data)
print('output: ', output)