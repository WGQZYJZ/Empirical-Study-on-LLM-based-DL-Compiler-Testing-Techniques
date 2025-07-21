'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.isinf\ntorch.isinf(input)\n'
import torch
x = torch.tensor([float('inf'), float('-inf'), float('nan'), float('nan')])
y = torch.isinf(x)
print(y)