'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.isneginf\ntorch.isneginf(input, *, out=None)\n'
import torch
input_data = torch.tensor([(- float('inf')), (- 1), (- 0.5), 0, 0.5, 1, float('inf')])
print(torch.isneginf(input_data))