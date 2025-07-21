'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.range\ntorch.range(start=0, end, step=1, *, out=None, dtype=None, layout=torch.strided, device=None, requires_grad=False)\n'
import torch
start = 0
end = 10
step = 1
torch.range(start, end, step)
'\nTask 4: Call the API torch.arange\ntorch.arange(start=0, end, step=1, *, out=None, dtype=None, layout=torch.strided, device=None, requires_grad=False)\n'
start = 0
end = 10
step = 1
torch.arange(start, end, step)
'\nTask 5: Call the API torch.linspace\ntorch.linspace(start, end, steps=100, *, out=None, dtype=None, layout=torch.strided, device=None, requires_grad=False)\n'
start = 0
end = 10
steps = 100
torch.linspace(start, end, steps)