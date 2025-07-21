'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.erfinv\ntorch.erfinv(input, *, out=None)\n'
import torch
print(torch.__version__)
input = torch.tensor([(- 1.0), 0.0, 1.0])
print(torch.erfinv(input))