'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.softmin\ntorch.nn.functional.softmin(input, dim=None, _stacklevel=3, dtype=None)\n'
import torch
import torch
input = torch.randn(2, 3)
output = torch.nn.functional.softmin(input, dim=0)
print(output)