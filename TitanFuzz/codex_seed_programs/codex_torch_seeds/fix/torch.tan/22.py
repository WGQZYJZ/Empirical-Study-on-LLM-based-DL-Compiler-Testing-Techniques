'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.tan\ntorch.tan(input, *, out=None)\n'
import torch
input_data = torch.tensor([0.0, 1.0, 2.0])
print('Input Data: ', input_data)
output_data = torch.tan(input_data)
print('Output Data: ', output_data)