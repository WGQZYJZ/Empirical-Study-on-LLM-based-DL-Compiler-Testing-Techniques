'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.flip\ntorch.flip(input, dims)\n'
import torch
input = torch.randn(3, 4)
print('The input data is: ', input)
output = torch.flip(input, [1])
print('The output data is: ', output)