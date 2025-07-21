'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.LongStorage\ntorch.LongStorage(*args, **kwargs)\n'
import torch
input_data = torch.randn(2, 3)
print('Input data: ', input_data)
size = torch.LongStorage(input_data.size())
print('Size: ', size)