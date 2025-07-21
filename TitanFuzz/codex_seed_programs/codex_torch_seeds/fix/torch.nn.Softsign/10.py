'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.Softsign\ntorch.nn.Softsign()\n'
import torch
input = torch.randn(2, 2)
print(input)
output = torch.nn.Softsign()(input)
print(output)