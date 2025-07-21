'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.relu\ntorch.nn.functional.relu(input, inplace=False)\n'
import torch
x = torch.randn(3, requires_grad=True)
y = torch.nn.functional.relu(x)
print(y)