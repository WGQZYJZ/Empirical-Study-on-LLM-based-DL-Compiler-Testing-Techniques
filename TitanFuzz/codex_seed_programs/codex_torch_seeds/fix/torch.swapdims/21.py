'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.swapdims\ntorch.swapdims(input, dim0, dim1)\n'
import torch
input_data = torch.randn(2, 3, 5)
print('Input data is: ', input_data)
output_data = torch.swapdims(input_data, 0, 1)
print('Output data is: ', output_data)