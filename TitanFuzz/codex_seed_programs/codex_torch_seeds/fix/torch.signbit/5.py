'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.signbit\ntorch.signbit(input, *, out=None)\n'
import torch
x = torch.tensor([(- 1), 0, 1], dtype=torch.float)
print(torch.signbit(x))