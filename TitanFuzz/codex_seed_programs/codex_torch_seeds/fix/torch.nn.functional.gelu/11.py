'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.gelu\ntorch.nn.functional.gelu(input)\n'
import torch
import torch.nn.functional as F
x = torch.randn(3, 3)
print(x)
y = F.gelu(x)
print(y)