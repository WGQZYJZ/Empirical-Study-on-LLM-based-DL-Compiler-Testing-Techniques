'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.hardsigmoid\ntorch.nn.functional.hardsigmoid(input, inplace=False)\n'
import torch
x = torch.tensor([(- 1.0), 0.0, 0.5, 1.0])
y = torch.nn.functional.hardsigmoid(x)
print(y)