'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.round\ntorch.round(input, *, out=None)\n'
import torch
data = torch.tensor([(- 1.2), (- 0.5), 0, 0.5, 1.2], dtype=torch.float)
print(torch.round(data))