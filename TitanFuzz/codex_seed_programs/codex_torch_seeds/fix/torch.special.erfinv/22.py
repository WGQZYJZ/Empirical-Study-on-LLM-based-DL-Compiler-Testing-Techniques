'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.special.erfinv\ntorch.special.erfinv(input, *, out=None)\n'
import torch
input_data = torch.tensor([(- 1), 0, 1])
print('Input:')
print(input_data)
output = torch.special.erfinv(input_data)
print('Output:')
print(output)