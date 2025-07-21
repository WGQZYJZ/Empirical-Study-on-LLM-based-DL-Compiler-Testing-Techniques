'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.softsign\ntorch.nn.functional.softsign(input)\n'
import torch
x = torch.randn(3, requires_grad=True)
y = torch.nn.functional.softsign(x)
print(y)