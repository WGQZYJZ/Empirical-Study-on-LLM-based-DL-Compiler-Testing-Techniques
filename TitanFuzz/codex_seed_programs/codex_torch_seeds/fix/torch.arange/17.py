'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.arange\ntorch.arange(start=0, end, step=1, *, out=None, dtype=None, layout=torch.strided, device=None, requires_grad=False)\n'
import torch
input_data = torch.arange(0, 10)
print(input_data)
'\nTask 4: Call the API torch.arange with start, end and step\ntorch.arange(start=0, end, step=1, *, out=None, dtype=None, layout=torch.strided, device=None, requires_grad=False)\n'
input_data = torch.arange(0, 10, 2)
print(input_data)
'\nTask 5: Call the API torch.arange with start, end, step and dtype\ntorch.arange(start=0, end, step=1, *, out=None, dtype=None, layout=torch.strided, device=None, requires_grad=False)\n'
input_data = torch.arange(0, 10, 2, dtype=torch.float)
print(input_data)