'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.arccos\ntorch.arccos(input, *, out=None)\n'
import torch
x = torch.tensor([0.0, 0.5, (- 0.5), 1.0, (- 1.0)])
print('Input:', x)
y = torch.arccos(x)
print('Output:', y)