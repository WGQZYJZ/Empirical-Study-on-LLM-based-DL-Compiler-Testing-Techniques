'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.mv\ntorch.mv(input, vec, *, out=None)\n'
import torch
input = torch.rand(3, 5)
vec = torch.rand(5)
output = torch.mv(input, vec)
print(output)