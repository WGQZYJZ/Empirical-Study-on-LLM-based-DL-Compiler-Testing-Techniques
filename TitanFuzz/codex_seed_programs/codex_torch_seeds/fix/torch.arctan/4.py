'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.arctan\ntorch.arctan(input, *, out=None)\n'
import torch
input_data = torch.tensor([0.5, 1.0, 1.5, 2.0])
arctan_output = torch.arctan(input_data)
print('Output: ', arctan_output)