'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.hardtanh_\ntorch.nn.functional.hardtanh_(input, min_val=-1., max_val=1.)\n'
import torch
import torch.nn.functional as F
import torch
import torch.nn.functional as F
input_data = torch.randn(2, 3)
F.hardtanh_(input_data, min_val=(- 1.0), max_val=1.0)
print('input_data: ', input_data)
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.hardtanh\ntorch.nn.functional.hardtanh(input, min_val=-1., max_val=1., inplace=False)\n'
import torch
import torch.nn.functional as F
import torch
import torch.nn.functional as F
input_data = torch.randn(2, 3)