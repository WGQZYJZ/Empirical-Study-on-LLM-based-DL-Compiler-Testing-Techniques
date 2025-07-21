'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.LongStorage\ntorch.LongStorage(*args, **kwargs)\n'
import torch
input_data = torch.randn(2, 3)
print(input_data)
input_data_size = torch.LongStorage(input_data.size())
print(input_data_size)