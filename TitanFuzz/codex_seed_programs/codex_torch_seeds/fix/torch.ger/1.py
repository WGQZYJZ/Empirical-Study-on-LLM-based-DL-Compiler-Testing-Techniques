'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.ger\ntorch.ger(input, vec2, *, out=None)\n'
import torch
vec1 = torch.tensor([1, 2])
vec2 = torch.tensor([3, 4])
out = torch.ger(vec1, vec2)
print(out)