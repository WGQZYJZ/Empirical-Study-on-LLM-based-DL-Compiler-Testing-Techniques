'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.linspace\ntorch.linspace(start, end, steps, *, out=None, dtype=None, layout=torch.strided, device=None, requires_grad=False)\n'
import torch
start = 0
end = 10
steps = 5
torch.linspace(start, end, steps)
torch.logspace(start, end, steps)
torch.arange(start, end, steps)