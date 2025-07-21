'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.chunk\ntorch.chunk(input, chunks, dim=0)\n'
import torch
import torch
input = torch.randn(4, 4)
print('Input: \n', input)
output1 = torch.chunk(input, 2, dim=0)
print('Output 1: \n', output1)
output2 = torch.chunk(input, 2, dim=1)
print('Output 2: \n', output2)