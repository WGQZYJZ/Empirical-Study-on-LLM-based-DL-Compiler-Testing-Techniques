'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.abs\ntorch.abs(input, *, out=None)\n'
import torch
input_data = torch.tensor([(- 1), (- 2), 3])
output = torch.abs(input_data)
print(output)