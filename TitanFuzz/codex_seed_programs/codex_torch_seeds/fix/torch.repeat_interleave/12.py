'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.repeat_interleave\ntorch.repeat_interleave(input, repeats, dim=None)\n'
import torch
input = torch.rand(3, 3)
repeats = torch.tensor([1, 2, 3])
print(torch.repeat_interleave(input, repeats, dim=0))