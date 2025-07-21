'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.celu\ntorch.nn.functional.celu(input, alpha=1., inplace=False)\n'
import torch
x = torch.randn(1, 2, 3, 4)
y = torch.nn.functional.celu(x)
print(y)