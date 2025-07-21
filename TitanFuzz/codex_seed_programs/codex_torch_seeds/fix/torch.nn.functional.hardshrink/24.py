'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.hardshrink\ntorch.nn.functional.hardshrink(input, lambd=0.5)\n'
import torch
x = torch.rand(5, 5)
print(x)
shrinked = torch.nn.functional.hardshrink(x)
print(shrinked)