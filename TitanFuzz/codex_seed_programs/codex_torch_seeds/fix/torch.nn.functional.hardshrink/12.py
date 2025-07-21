'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.hardshrink\ntorch.nn.functional.hardshrink(input, lambd=0.5)\n'
import torch
input = torch.randn(4, 4)
print(input)
import torch
input = torch.randn(4, 4)
print(torch.nn.functional.hardshrink(input, lambd=0.5))