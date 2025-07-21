'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.absolute\ntorch.absolute(input, *, out=None)\n'
import torch
input_data = torch.tensor([[(- 1), (- 2), (- 3)], [1, 2, 3]])
output_data = torch.absolute(input_data)
print('input_data:', input_data)
print('output_data:', output_data)