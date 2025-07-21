'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.leaky_relu_\ntorch.nn.functional.leaky_relu_(input, negative_slope=0.01)\n'
import torch
import torch
x = torch.randn(3, 3)
y = torch.nn.functional.leaky_relu_(x, negative_slope=0.01)
print(y)