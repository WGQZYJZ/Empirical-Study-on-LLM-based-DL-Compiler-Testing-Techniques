'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.swapdims\ntorch.swapdims(input, dim0, dim1)\n'
import torch
input_data = torch.randn(1, 2, 3, 4)
output_data = torch.swapdims(input_data, dim0=2, dim1=3)
print('output_data: ', output_data)