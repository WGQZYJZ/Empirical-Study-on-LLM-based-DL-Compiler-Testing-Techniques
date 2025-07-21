'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.qr\ntorch.qr(input, some=True, *, out=None)\n'
import torch
input_data = torch.randn(3, 5)
output_data = torch.qr(input_data)
print('input_data: ', input_data)
print('output_data: ', output_data)