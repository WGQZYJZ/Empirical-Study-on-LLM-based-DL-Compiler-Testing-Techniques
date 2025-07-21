'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.relu\ntorch.nn.functional.relu(input, inplace=False)\n'
import torch
x = torch.randn(1, 3, 4, 4)
print(x)
y = torch.nn.functional.relu(x)
print(y)