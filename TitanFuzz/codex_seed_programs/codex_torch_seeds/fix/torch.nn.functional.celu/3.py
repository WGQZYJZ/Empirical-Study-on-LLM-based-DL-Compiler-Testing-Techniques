'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.celu\ntorch.nn.functional.celu(input, alpha=1., inplace=False)\n'
import torch
import torch.nn.functional as F
import torch
input = torch.randn(1, 1, 3, 3)
F.celu(input)