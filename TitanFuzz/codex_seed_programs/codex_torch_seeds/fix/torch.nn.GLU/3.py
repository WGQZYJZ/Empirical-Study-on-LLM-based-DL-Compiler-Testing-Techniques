'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.GLU\ntorch.nn.GLU(dim=-1)\n'
import torch
input = torch.randn(10, 4, 6)
print(input)
glu = torch.nn.GLU(dim=(- 1))
output = glu(input)
print(output)