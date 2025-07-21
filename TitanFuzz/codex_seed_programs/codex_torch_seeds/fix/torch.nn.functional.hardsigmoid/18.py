'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.hardsigmoid\ntorch.nn.functional.hardsigmoid(input, inplace=False)\n'
import torch
input = torch.randn(2, 3)
torch.nn.functional.hardsigmoid(input)
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.hardtanh\ntorch.nn.functional.hardtanh(input, min_val=-1.0, max_val=1.0, inplace=False)\n'
import torch
input = torch.randn(2, 3)
torch.nn.functional.hardtanh(input, min_val=(- 1.0), max_val=1.0)