'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.lcm\ntorch.lcm(input, other, *, out=None)\n'
import torch
input = torch.tensor([20, 10, 5])
other = torch.tensor([2, 3, 4])
lcm = torch.lcm(input, other)
print(lcm)
'\nTask 4: Call the API torch.gcd\ntorch.gcd(input, other, *, out=None)\n'
gcd = torch.gcd(input, other)
print(gcd)