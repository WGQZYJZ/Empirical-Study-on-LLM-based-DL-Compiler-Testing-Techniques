'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.relu6\ntorch.nn.functional.relu6(input, inplace=False)\n'
import torch
import torch.nn.functional as F
x = torch.randn(3, 3)
print(x)
print(F.relu6(x))
print(F.relu6(x, inplace=True))
print(x)