'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.hardtanh\ntorch.nn.functional.hardtanh(input, min_val=-1., max_val=1., inplace=False)\n'
import torch
import torch.nn.functional as F
input = torch.randn(3, 5)
print('input:\n', input)
output = F.hardtanh(input)
print('output:\n', output)