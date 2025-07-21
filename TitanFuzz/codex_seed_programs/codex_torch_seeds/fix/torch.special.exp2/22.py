'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.special.exp2\ntorch.special.exp2(input, *, out=None)\n'
import torch
input = torch.tensor([(- 1), 0, 1])
output = torch.special.exp2(input)
print(output)