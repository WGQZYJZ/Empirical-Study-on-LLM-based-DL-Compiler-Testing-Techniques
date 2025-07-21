'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.Softsign\ntorch.nn.Softsign()\n'
import torch
input_data = torch.tensor([(- 1.0), (- 0.5), 0, 0.5, 1.0])
softsign = torch.nn.Softsign()
output_data = softsign(input_data)
print('input_data: ', input_data)
print('output_data: ', output_data)