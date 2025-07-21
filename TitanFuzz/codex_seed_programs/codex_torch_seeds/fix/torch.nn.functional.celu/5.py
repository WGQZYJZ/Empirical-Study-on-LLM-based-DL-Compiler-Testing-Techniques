'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.celu\ntorch.nn.functional.celu(input, alpha=1., inplace=False)\n'
import torch
import torch.nn.functional as F
input = torch.randn(5, 5)
import torch
input = torch.randn(5, 5)
output = F.celu(input)
print(output)