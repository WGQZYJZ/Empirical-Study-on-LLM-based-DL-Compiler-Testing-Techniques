'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.linspace\ntorch.linspace(start, end, steps, *, out=None, dtype=None, layout=torch.strided, device=None, requires_grad=False)\n'
import torch
start = 0
end = 10
steps = 5
x = torch.linspace(start, end, steps)
print(x)
'\nTask 4: Call the API torch.logspace\ntorch.logspace(start, end, steps, base=10.0, out=None, dtype=None, layout=torch.strided, device=None, requires_grad=False)\n'
start = 0
end = 10
steps = 5
x = torch.logspace(start, end, steps)
print(x)
'\nTask 5: Call the API torch.arange\ntorch.arange(start, end, step=1, out=None, dtype=None, layout=torch.strided, device=None, requires_grad=False)\n'
start = 0
end = 10
step = 1
x = torch.arange(start, end, step)
print(x)