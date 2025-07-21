'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.gather\ntorch.gather(input, dim, index, *, sparse_grad=False, out=None)\n'
import torch
data = torch.tensor([[1, 2], [3, 4]])
indices = torch.tensor([[0, 1], [1, 0]])
torch.gather(data, dim=0, index=indices)