'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.range\ntorch.range(start=0, end, step=1, *, out=None, dtype=None, layout=torch.strided, device=None, requires_grad=False)\n'
import torch
print('Task 1: import PyTorch')
print('Task 2: Generate input data')
print('Task 3: Call the API torch.range')
start = 0
end = 10
step = 1
print('start = ', start)
print('end = ', end)
print('step = ', step)
print('torch.range(start, end, step) = ', torch.range(start, end, step))