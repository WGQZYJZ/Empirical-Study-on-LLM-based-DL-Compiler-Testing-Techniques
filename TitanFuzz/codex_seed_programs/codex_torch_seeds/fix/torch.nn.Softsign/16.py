'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.Softsign\ntorch.nn.Softsign()\n'
import torch
input_data = torch.tensor([(- 1.0), (- 0.5), 0.0, 0.5, 1.0])
print('Input data: ', input_data)
softsign = torch.nn.Softsign()
output = softsign(input_data)
print('Output: ', output)