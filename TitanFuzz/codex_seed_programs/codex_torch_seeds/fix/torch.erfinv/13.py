'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.erfinv\ntorch.erfinv(input, *, out=None)\n'
import torch
input_data = torch.tensor([(- 0.5), 0.5])
output_data = torch.erfinv(input_data)
print(output_data)