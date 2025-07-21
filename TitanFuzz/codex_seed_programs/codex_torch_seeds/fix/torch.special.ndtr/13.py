'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.special.ndtr\ntorch.special.ndtr(input, *, out=None)\n'
import torch
data = torch.randn(10, 5)
print(data)
torch.special.ndtr(data)