'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.signbit\ntorch.signbit(input, *, out=None)\n'
import torch
input_data = torch.randn(5, 3)
print('input_data: {}'.format(input_data))
result = torch.signbit(input_data)
print('result: {}'.format(result))