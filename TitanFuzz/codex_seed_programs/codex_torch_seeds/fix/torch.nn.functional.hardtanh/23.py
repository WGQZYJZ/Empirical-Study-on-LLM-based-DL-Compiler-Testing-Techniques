'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.hardtanh\ntorch.nn.functional.hardtanh(input, min_val=-1., max_val=1., inplace=False)\n'
import torch
x = torch.randn(3, 4)
y = torch.nn.functional.hardtanh(x)
print(x)
print(y)