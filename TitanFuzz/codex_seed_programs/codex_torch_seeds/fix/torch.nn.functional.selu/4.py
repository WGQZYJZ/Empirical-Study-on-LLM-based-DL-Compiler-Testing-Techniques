'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.selu\ntorch.nn.functional.selu(input, inplace=False)\n'
import torch
x = torch.randn(5, 5)
print(x)
y = torch.nn.functional.selu(x)
print(y)
y = torch.nn.functional.selu(x, inplace=True)
print(y)
y = torch.nn.functional.selu(x)
print(y)