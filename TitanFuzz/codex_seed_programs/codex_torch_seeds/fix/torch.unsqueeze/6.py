'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.unsqueeze\ntorch.unsqueeze(input, dim)\n'
import torch
input_data = torch.tensor([1, 2, 3, 4, 5])
output_data = torch.unsqueeze(input_data, 0)
print('Input:', input_data)
print('Output:', output_data)