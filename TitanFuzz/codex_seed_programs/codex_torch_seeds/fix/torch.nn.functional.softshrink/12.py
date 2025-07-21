'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.softshrink\ntorch.nn.functional.softshrink(input, lambd=0.5)\n'
import torch
import torch
x = torch.randn(2, 3)
torch.nn.functional.softshrink(x)
torch.nn.functional.softshrink(x, lambd=0.5)
torch.nn.functional.softshrink(x, lambd=1.0)
torch.nn.functional.softshrink(x, lambd=1.5)
torch.nn.functional.softshrink(x, lambd=2.0)