'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.init.zeros_\ntorch.nn.init.zeros_(tensor)\n'
import torch
input = torch.randn(2, 2)
print(input)
torch.nn.init.zeros_(input)
print(input)