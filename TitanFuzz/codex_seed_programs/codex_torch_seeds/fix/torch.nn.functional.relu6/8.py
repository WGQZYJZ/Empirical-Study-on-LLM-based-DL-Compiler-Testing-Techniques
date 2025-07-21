'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.relu6\ntorch.nn.functional.relu6(input, inplace=False)\n'
import torch
input = torch.randn(5, 5)
output = torch.nn.functional.relu6(input)
print('Input:')
print(input)
print('Output:')
print(output)