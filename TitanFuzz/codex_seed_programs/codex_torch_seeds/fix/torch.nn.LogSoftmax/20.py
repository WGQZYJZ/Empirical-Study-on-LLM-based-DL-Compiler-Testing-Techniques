'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.LogSoftmax\ntorch.nn.LogSoftmax(dim=None)\n'
import torch
import torch
input_data = torch.randn(2, 3)
print('input_data: ', input_data)
output_data = torch.nn.LogSoftmax(dim=1)(input_data)
print('output_data: ', output_data)