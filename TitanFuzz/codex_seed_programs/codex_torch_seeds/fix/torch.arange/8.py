'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.arange\ntorch.arange(start=0, end, step=1, *, out=None, dtype=None, layout=torch.strided, device=None, requires_grad=False)\n'
import torch
input_data = torch.arange(start=0, end=10, step=1)
print(input_data)
'\nTask 4: Call the API torch.linspace\ntorch.linspace(start, end, steps=100, *, out=None, dtype=None, layout=torch.strided, device=None, requires_grad=False)\n'
input_data = torch.linspace(start=0, end=10, steps=10)
print(input_data)
'\nTask 5: Call the API torch.logspace\ntorch.logspace(start, end, steps=100, base=10.0, out=None, dtype=None, layout=torch.strided, device=None, requires_grad=False)\n'
input_data = torch.logspace(start=0, end=10, steps=10, base=10)
print(input_data)