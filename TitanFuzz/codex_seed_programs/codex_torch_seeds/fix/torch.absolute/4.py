'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.absolute\ntorch.absolute(input, *, out=None)\n'
import torch
input = torch.tensor([(- 1), (- 2), 3])
output = torch.absolute(input)
print(output)