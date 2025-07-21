'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.neg\ntorch.neg(input, *, out=None)\n'
import torch
input_data = torch.randn(2, 3)
print('Input data: ', input_data)
output_data = torch.neg(input_data)
print('Output data: ', output_data)