'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.selu\ntorch.nn.functional.selu(input, inplace=False)\n'
import torch
import torch
input_data = torch.tensor([[(- 1), 0, 1], [2, 3, 4]], dtype=torch.float)
output_data = torch.nn.functional.selu(input_data)
print('input_data:', input_data)
print('output_data:', output_data)