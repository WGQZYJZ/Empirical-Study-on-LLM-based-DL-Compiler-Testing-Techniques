'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.atan\ntorch.atan(input, *, out=None)\n'
import torch
import torch
input_data = torch.tensor([0.0, 1.0, (- 1.0), 0.5, (- 0.5)])
output = torch.atan(input_data)
print(output)