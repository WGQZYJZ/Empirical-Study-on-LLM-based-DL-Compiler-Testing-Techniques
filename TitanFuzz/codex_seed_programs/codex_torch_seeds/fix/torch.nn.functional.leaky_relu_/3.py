'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.leaky_relu_\ntorch.nn.functional.leaky_relu_(input, negative_slope=0.01)\n'
import torch
x = torch.linspace((- 2), 2, 100)
y = torch.nn.functional.leaky_relu_(x)
print(x)
print(y)