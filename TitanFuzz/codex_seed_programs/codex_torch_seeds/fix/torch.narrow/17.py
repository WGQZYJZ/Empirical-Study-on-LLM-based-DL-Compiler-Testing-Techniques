'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.narrow\ntorch.narrow(input, dim, start, length)\n'
import torch
input_data = torch.arange(1, 11)
result = torch.narrow(input_data, 0, 0, 4)
print('Result: ', result)