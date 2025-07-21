'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.Softshrink\ntorch.nn.Softshrink(lambd=0.5)\n'
import torch
x = torch.rand(1, 2, 3, 3, requires_grad=True)
softshrink = torch.nn.Softshrink(lambd=0.5)
output = softshrink(x)
print(output)
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.Softsign\ntorch.nn.Softsign()\n'
import torch
x = torch.rand(1, 2, 3, 3, requires_grad=True)
softsign = torch.nn.Softsign()
output = softsign(x)
print(output)