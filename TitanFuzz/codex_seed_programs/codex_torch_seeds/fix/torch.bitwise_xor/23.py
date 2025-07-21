'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.bitwise_xor\ntorch.bitwise_xor(input, other, *, out=None)\n'
import torch
a = torch.randint(low=0, high=2, size=(4, 4), dtype=torch.uint8)
b = torch.randint(low=0, high=2, size=(4, 4), dtype=torch.uint8)
print(a)
print(b)
c = torch.bitwise_xor(a, b)
print(c)