'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.imag\ntorch.imag(input)\n'
import torch
input = torch.tensor([(1 + 1j), (2 + 2j), (3 + 3j), (4 + 4j)])
output = torch.imag(input)
print('Input: {}'.format(input))
print('Output: {}'.format(output))