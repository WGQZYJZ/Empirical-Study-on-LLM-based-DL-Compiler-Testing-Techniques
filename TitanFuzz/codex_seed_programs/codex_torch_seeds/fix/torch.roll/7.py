'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.roll\ntorch.roll(input, shifts, dims=None)\n'
import torch
x = torch.arange(0, 9, dtype=torch.float)
x = x.reshape(3, 3)
print(torch.roll(x, 1, dims=1))
print(torch.roll(x, 1, dims=0))