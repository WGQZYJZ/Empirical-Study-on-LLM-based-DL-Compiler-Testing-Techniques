'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.lcm\ntorch.lcm(input, other, *, out=None)\n'
import torch
x = torch.tensor([5, 25, 125])
y = torch.tensor([3, 15, 75])
result = torch.lcm(x, y)
print(result)