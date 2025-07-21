'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.init.dirac_\ntorch.nn.init.dirac_(tensor, groups=1)\n'
import torch
input_tensor = torch.randn(2, 3, 3, 3)
print(input_tensor)
torch.nn.init.dirac_(input_tensor, groups=1)
print(input_tensor)