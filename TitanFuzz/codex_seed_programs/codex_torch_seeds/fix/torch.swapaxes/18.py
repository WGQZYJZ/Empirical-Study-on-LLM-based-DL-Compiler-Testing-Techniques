'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.swapaxes\ntorch.swapaxes(input, axis0, axis1)\n'
import torch
input_data = torch.arange(0, 24).view(2, 3, 4)
print(input_data)
output_data = torch.swapaxes(input_data, 1, 2)
print(output_data)