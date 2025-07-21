'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.clip\ntorch.clip(input, min=None, max=None, *, out=None)\n'
import torch
import torch
input_data = torch.tensor([(- 1.0), 0.0, 1.0, 2.0, 3.0, 4.0])
print('input_data =', input_data)
output_data = torch.clip(input_data, min=1.0, max=3.0)
print('output_data =', output_data)