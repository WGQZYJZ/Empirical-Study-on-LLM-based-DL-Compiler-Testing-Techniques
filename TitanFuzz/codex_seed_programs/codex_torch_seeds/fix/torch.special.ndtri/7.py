'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.special.ndtri\ntorch.special.ndtri(input, *, out=None)\n'
import torch
import torch
input_data = torch.tensor([0.25, 0.5, 0.75])
output_data = torch.special.ndtri(input_data)
print('Input:', input_data)
print('Output:', output_data)