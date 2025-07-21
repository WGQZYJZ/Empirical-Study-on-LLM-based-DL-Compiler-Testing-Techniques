'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.arange\ntorch.arange(start=0, end, step=1, *, out=None, dtype=None, layout=torch.strided, device=None, requires_grad=False)\n'
import torch
input_data = torch.arange(1, 17, dtype=torch.float).view(4, 4)
print(input_data)
print(input_data.size())
'\nTask 4: Call the API torch.zeros_like\ntorch.zeros_like(input, dtype=None, layout=None, device=None, requires_grad=False)\n'
input_data = torch.arange(1, 17, dtype=torch.float).view(4, 4)
output_data = torch.zeros_like(input_data)
print(output_data)
'\nTask 5: Call the API torch.ones_like\ntorch.ones_like(input, dtype=None, layout=None, device=None, requires_grad=False)\n'
input_data = torch.arange(1, 17, dtype=torch.float).view(4, 4)
output_data = torch.ones_like(input_data)
print(output_data)