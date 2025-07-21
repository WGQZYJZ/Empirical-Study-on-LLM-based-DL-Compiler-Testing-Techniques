'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.logspace\ntorch.logspace(start, end, steps, base=10.0, *, out=None, dtype=None, layout=torch.strided, device=None, requires_grad=False)\n'
import torch
start = 0
end = 10
steps = 5
print('Input:')
print('start = ', start)
print('end = ', end)
print('steps = ', steps)
print('Output:')
print(torch.logspace(start, end, steps))
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.linspace\ntorch.linspace(start, end, steps=100, *, out=None, dtype=None, layout=torch.strided, device=None, requires_grad=False) → Tensor\n'
import torch
start = 0
end = 10
steps = 5
print('Input:')
print('start = ', start)
print('end = ', end)
print('steps = ', steps)
print('Output:')
print(torch.linspace(start, end, steps))