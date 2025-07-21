'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.celu\ntorch.nn.functional.celu(input, alpha=1., inplace=False)\n'
import torch
import torch
input = torch.randn(4, 4)
torch.nn.functional.celu(input, alpha=1.0, inplace=False)
torch.nn.functional.celu(input, alpha=0.5, inplace=False)
torch.nn.functional.celu(input, alpha=0.1, inplace=False)
torch.nn.functional.celu(input, alpha=0.01, inplace=False)
torch.nn.functional.celu(input, alpha=0.001, inplace=False)
torch.nn.functional.celu(input, alpha=0.0001, inplace=False)