'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.gcd\ntorch.gcd(input, other, *, out=None)\n'
import torch
x = torch.tensor(10)
y = torch.tensor(5)
print(torch.gcd(x, y))