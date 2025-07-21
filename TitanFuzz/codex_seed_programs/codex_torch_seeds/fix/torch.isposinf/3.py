'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.isposinf\ntorch.isposinf(input, *, out=None)\n'
import torch
input_data = torch.tensor([float('inf'), float('-inf'), float('nan')])
print(torch.isposinf(input_data))
input_data = torch.tensor([float('inf'), float('-inf'), float('nan'), 1.0])
print(torch.isposinf(input_data))