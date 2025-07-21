'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.log2\ntorch.log2(input, *, out=None)\n'
import torch
input_data = torch.tensor([2, 4, 8, 16], dtype=torch.float32)
output_data = torch.log2(input_data)
print('Input:', input_data)
print('Output:', output_data)