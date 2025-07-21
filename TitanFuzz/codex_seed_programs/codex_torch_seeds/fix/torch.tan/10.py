'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.tan\ntorch.tan(input, *, out=None)\n'
import torch
input_data = torch.randn(1, 3, 3)
print('Input data is: ', input_data)
output = torch.tan(input_data)
print('Output data is: ', output)