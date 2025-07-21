'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.selu\ntorch.nn.functional.selu(input, inplace=False)\n'
import torch
x = torch.randn(2, 3)
print(x)
y = torch.nn.functional.selu(x)
print(y)