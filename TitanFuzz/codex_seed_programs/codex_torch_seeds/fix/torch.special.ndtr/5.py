'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.special.ndtr\ntorch.special.ndtr(input, *, out=None)\n'
import torch
input = torch.randn(1, 1)
output = torch.special.ndtr(input)
print(output)