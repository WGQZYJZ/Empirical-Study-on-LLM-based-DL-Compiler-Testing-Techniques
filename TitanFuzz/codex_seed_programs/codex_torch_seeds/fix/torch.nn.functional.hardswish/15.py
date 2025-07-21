'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.hardswish\ntorch.nn.functional.hardswish(input, inplace=False)\n'
import torch
import torch
input = torch.randn(2, 3)
torch.nn.functional.hardswish(input)
torch.nn.functional.hardswish(input, inplace=True)