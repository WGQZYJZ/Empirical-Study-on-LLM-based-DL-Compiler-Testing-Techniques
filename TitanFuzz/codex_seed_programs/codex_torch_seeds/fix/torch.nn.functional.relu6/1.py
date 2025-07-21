'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.relu6\ntorch.nn.functional.relu6(input, inplace=False)\n'
import torch
x = torch.randn(3, 5)
print(x)
y = torch.nn.functional.relu6(x)
print(y)