'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.log2\ntorch.log2(input, *, out=None)\n'
import torch
import torch
input_data = torch.tensor([1.0, 2.0, 4.0, 8.0, 16.0, 32.0])
output = torch.log2(input_data)
print('Input: ', input_data)
print('Output: ', output)