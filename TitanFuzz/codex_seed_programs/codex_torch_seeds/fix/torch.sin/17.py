'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.sin\ntorch.sin(input, *, out=None)\n'
import torch
x = torch.tensor([0, 30, 60, 90, 120, 150, 180, 210, 240, 270, 300, 330])
y = torch.sin(x)
print(y)