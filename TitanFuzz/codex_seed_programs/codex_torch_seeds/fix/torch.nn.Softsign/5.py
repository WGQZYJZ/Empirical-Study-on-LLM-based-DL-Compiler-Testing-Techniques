'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.Softsign\ntorch.nn.Softsign()\n'
import torch
import torch
input = torch.randn(1, 3)
output = torch.nn.Softsign()(input)
print(output)