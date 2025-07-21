'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.GLU\ntorch.nn.GLU(dim=-1)\n'
import torch
input_data = torch.randn(3, 4)
print(input_data)
glu = torch.nn.GLU(dim=(- 1))
output = glu(input_data)
print(output)