'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.log2\ntorch.log2(input, *, out=None)\n'
import torch
input_data = torch.tensor([1.0, 2.0, 4.0, 8.0])
output = torch.log2(input_data)
print('The input data is:', input_data)
print('The output of log2 is:', output)