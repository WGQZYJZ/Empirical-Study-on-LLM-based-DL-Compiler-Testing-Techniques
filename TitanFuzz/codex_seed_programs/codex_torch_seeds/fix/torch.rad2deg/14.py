'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.rad2deg\ntorch.rad2deg(input, *, out=None)\n'
import torch
import math
input = torch.tensor([0, (math.pi / 2), math.pi, ((3 * math.pi) / 2), (2 * math.pi)])
output = torch.rad2deg(input)
print(output)