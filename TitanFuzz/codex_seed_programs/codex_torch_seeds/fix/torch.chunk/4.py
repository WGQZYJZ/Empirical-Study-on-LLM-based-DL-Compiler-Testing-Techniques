'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.chunk\ntorch.chunk(input, chunks, dim=0)\n'
import torch
x = torch.tensor([[1, 2, 3], [4, 5, 6]])
torch.chunk(x, 2, dim=1)