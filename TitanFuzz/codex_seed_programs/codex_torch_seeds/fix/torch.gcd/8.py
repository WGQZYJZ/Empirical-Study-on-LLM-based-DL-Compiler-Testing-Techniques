'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.gcd\ntorch.gcd(input, other, *, out=None)\n'
import torch
a = torch.randint(low=0, high=100, size=(1,))
b = torch.randint(low=0, high=100, size=(1,))
print(a, b)
gcd = torch.gcd(a, b)
print(gcd)