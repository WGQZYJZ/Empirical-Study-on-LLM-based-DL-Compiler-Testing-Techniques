'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.hardswish\ntorch.nn.functional.hardswish(input, inplace=False)\n'
import torch
import torch.nn as nn
import torch.nn.functional as F
input_data = torch.randn(3, 3)
output = F.hardswish(input_data)
print(output)
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.hardtanh\ntorch.nn.functional.hardtanh(input, min_val=-1, max_val=1, inplace=False)\n'
import torch
import torch.nn as nn
import torch.nn.functional as F
input_data = torch.randn(3, 3)
output = F.hardtanh(input_data)
print(output)