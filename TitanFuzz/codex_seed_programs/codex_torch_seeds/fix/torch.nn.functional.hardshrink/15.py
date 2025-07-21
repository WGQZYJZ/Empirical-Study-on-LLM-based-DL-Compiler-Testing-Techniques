'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.hardshrink\ntorch.nn.functional.hardshrink(input, lambd=0.5)\n'
import torch
x = torch.tensor([(- 2.0), (- 1.0), 0.0, 1.0, 2.0])
print(torch.nn.functional.hardshrink(x, lambd=0.5))
print(torch.nn.functional.hardshrink(x, lambd=0.1))
print(torch.nn.functional.hardshrink(x, lambd=0.9))