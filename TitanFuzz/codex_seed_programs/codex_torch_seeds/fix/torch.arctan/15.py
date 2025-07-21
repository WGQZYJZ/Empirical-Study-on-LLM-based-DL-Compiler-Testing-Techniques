'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.arctan\ntorch.arctan(input, *, out=None)\n'
import torch
import math
x = torch.tensor([0, (math.pi / 4), (math.pi / 2), ((3 * math.pi) / 4), math.pi])
print(x)
y = torch.arctan(x)
print(y)