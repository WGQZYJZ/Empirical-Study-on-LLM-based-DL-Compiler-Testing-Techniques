'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.le\ntorch.le(input, other, *, out=None)\n'
import torch
input_data = torch.tensor([(- 1), 2])
output_data = torch.le(input_data, 0)
print(output_data)