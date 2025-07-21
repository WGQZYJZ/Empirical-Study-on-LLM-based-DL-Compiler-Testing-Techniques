'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.fmod\ntorch.fmod(input, other, *, out=None)\n'
import torch
a = torch.tensor([(- 3.1415), 3.1415])
b = torch.tensor([2.7183])
print(torch.fmod(a, b))