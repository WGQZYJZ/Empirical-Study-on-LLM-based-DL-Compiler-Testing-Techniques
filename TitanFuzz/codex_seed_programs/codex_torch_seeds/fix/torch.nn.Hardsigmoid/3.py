'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.Hardsigmoid\ntorch.nn.Hardsigmoid(inplace=False)\n'
import torch
input_data = torch.tensor([(- 1.0), (- 0.5), 0.0, 0.5, 1.0])
hardsigmoid = torch.nn.Hardsigmoid()
output = hardsigmoid(input_data)
print('input data: ', input_data)
print('output data: ', output)