'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.Softsign\ntorch.nn.Softsign()\n'
import torch
x = torch.tensor([(- 2), (- 1), 0, 1, 2])
y = torch.nn.Softsign()(x)
print('The result of softsign function: ', y)