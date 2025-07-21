'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.rad2deg\ntorch.rad2deg(input, *, out=None)\n'
import torch
import math
input_data = torch.rand(1)
radian = (math.pi * input_data)
degree = torch.rad2deg(radian)
print(degree)