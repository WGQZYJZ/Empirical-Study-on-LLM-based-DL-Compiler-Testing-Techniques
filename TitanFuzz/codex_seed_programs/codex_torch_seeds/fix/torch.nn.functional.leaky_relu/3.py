'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.leaky_relu\ntorch.nn.functional.leaky_relu(input, negative_slope=0.01, inplace=False)\n'
import torch
x = torch.randn(3, 3)
y = torch.nn.functional.leaky_relu(x, negative_slope=0.01, inplace=False)
print(y)