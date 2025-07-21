'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.softshrink\ntorch.nn.functional.softshrink(input, lambd=0.5)\n'
import torch
import torch
input = torch.randn(1, 3, 5, 5)
output = torch.nn.functional.softshrink(input, lambd=0.5)
print(output)