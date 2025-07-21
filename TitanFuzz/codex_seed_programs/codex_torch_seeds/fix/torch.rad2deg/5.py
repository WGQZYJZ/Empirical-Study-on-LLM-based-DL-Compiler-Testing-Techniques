'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.rad2deg\ntorch.rad2deg(input, *, out=None)\n'
import torch
import math
input = torch.tensor([(math.pi / 2), (math.pi / 4), (math.pi / 8), (math.pi / 16)])
output = torch.rad2deg(input)
print(output)