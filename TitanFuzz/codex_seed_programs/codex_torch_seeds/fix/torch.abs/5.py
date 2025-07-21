'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.abs\ntorch.abs(input, *, out=None)\n'
import torch
data = torch.tensor([(- 1), (- 2), 3, 4, (- 5)])
print(torch.abs(data))