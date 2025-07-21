'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.mv\ntorch.mv(input, vec, *, out=None)\n'
import torch
input = torch.randn(2, 3)
print(input)
output = torch.mv(input, torch.tensor([1.0, 2.0, 3.0]))
print(output)