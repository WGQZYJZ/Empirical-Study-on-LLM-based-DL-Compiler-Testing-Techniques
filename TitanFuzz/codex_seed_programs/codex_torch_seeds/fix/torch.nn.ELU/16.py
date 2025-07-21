'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.ELU\ntorch.nn.ELU(alpha=1.0, inplace=False)\n'
import torch
input_data = torch.randn(1, 1, 3, 3)
elu = torch.nn.ELU()
output = elu(input_data)
print(output)
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.Hardshrink\ntorch.nn.Hardshrink(lambd=0.5)\n'
import torch
input_data = torch.randn(1, 1, 3, 3)
hardshrink = torch.nn.Hardshrink()
output = hardshrink(input_data)
print(output)
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.Hardtanh\ntorch.nn.Hardtanh(min_val=-1.0, max_val=1.0, inplace=False)\n'
import torch
input_data = torch