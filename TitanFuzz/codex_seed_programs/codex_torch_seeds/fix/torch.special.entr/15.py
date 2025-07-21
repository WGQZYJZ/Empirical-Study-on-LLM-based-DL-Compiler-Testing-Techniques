'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.special.entr\ntorch.special.entr(input, *, out=None)\n'
import torch
import torch
x = torch.tensor([1, 2, 3])
torch.special.entr(x)
torch.special.entr(x, out=torch.empty(x.size()))