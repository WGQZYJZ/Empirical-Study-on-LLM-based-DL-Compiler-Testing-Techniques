'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.vsplit\ntorch.vsplit(input, indices_or_sections)\n'
import torch
x = torch.arange(16, dtype=torch.float32).reshape(4, 4)
print(x)
y = torch.vsplit(x, 2)
print(y)
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.chunk\ntorch.chunk(input, chunks, dim)\n'
import torch
x = torch.arange(16, dtype=torch.float32).reshape(4, 4)
print(x)
y = torch.chunk(x, 2, dim=1)
print(y)
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.split\ntorch.split(input, split_size, dim)\n'
import torch