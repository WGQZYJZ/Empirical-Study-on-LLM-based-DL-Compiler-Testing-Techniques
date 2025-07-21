'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.lcm\ntorch.lcm(input, other, *, out=None)\n'
import torch
x = torch.tensor([12, 6, 15, 4, 8], dtype=torch.int32)
y = torch.tensor([10, 20, 30, 40, 50], dtype=torch.int32)
z = torch.lcm(x, y)
print(z)