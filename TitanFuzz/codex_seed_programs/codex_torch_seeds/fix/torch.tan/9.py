'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.tan\ntorch.tan(input, *, out=None)\n'
import torch
input_data = torch.tensor([(- 1), 0, 1])
output_data = torch.tan(input_data)
print('Input Data:', input_data)
print('Output Data:', output_data)