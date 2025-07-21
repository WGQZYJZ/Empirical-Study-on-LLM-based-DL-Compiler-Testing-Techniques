'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.gcd\ntorch.gcd(input, other, *, out=None)\n'
import torch
input = torch.randint(1, 10, (3, 3), dtype=torch.long)
other = torch.randint(1, 10, (3, 3), dtype=torch.long)
torch.gcd(input, other)