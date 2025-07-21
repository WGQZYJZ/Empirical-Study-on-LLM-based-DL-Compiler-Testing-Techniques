'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.roll\ntorch.roll(input, shifts, dims=None)\n'
import torch
import torch
x = torch.tensor([[1, 2, 3], [4, 5, 6]])
print(x)
y = torch.roll(x, 1, dims=1)
print(y)
y = torch.roll(x, (- 1), dims=1)
print(y)