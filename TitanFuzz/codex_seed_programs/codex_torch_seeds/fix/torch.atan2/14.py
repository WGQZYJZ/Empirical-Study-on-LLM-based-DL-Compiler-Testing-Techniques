'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.atan2\ntorch.atan2(input, other, *, out=None)\n'
import torch
input = torch.tensor([1.0, 0.0, (- 1.0)])
other = torch.tensor([0.0, 1.0, 0.0])
torch.atan2(input, other)