'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.absolute\ntorch.absolute(input, *, out=None)\n'
import torch
x = torch.tensor([(- 1), (- 2), 3])
print(torch.absolute(x))
x = torch.tensor([(- 1), (- 2), 3], dtype=torch.float32)
print(torch.abs(x))