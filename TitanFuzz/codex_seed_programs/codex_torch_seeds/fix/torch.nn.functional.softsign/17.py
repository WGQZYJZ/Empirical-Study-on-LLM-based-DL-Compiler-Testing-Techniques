'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.softsign\ntorch.nn.functional.softsign(input)\n'
import torch
input = torch.tensor([(- 1), (- 0.5), 0, 0.5, 1])
output = torch.nn.functional.softsign(input)
print('The input data:\n', input)
print('The output data:\n', output)