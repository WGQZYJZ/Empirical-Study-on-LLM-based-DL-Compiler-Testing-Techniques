'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.dsplit\ntorch.dsplit(input, indices_or_sections)\n'
import torch
input = torch.randn(2, 3, 4)
print(input)
print('\nSplitting along dimension 1')
output1 = torch.dsplit(input, 2)
print(output1)
print('\nSplitting along dimension 1')
output2 = torch.dsplit(input, [1, 2])
print(output2)