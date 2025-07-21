'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.hardshrink\ntorch.nn.functional.hardshrink(input, lambd=0.5)\n'
import torch
import torch.nn.functional as F
input = torch.randn(1, 10, dtype=torch.float32)
print('input =', input)
output = F.hardshrink(input)
print('output =', output)