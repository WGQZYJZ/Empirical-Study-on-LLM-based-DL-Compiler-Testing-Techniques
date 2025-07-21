'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.abs\ntorch.abs(input, *, out=None)\n'
import torch
input_data = torch.tensor([(- 1), (- 2), 3, 4])
abs_output = torch.abs(input_data)
print(abs_output)