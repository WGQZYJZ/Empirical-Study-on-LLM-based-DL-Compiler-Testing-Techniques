'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.acos\ntorch.acos(input, *, out=None)\n'
import torch
import torch
input_data = torch.tensor([1, (- 1), 0.5, (- 0.5)])
output = torch.acos(input_data)
print(output)