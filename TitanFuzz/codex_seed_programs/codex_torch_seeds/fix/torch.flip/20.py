'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.flip\ntorch.flip(input, dims)\n'
import torch
input_data = torch.randn(3, 4)
print('Input data:')
print(input_data)
output = torch.flip(input_data, [1])
print('Output:')
print(output)