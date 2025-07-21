'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.special.erfcx\ntorch.special.erfcx(input, *, out=None)\n'
import torch
input = torch.randn(2, 3, dtype=torch.float)
print('input: ', input)
output = torch.special.erfcx(input)
print('output: ', output)