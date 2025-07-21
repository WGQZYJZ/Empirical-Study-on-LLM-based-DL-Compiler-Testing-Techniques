'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.celu\ntorch.nn.functional.celu(input, alpha=1., inplace=False)\n'
import torch
import torch.nn.functional as F
print(torch.__version__)
input = torch.randn(100, 100)
print(input)
output = F.celu(input, alpha=1.0, inplace=False)
print(output)