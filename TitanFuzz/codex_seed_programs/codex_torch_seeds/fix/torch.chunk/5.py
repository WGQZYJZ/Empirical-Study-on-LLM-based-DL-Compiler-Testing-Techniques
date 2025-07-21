'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.chunk\ntorch.chunk(input, chunks, dim=0)\n'
import torch
input = torch.randn(8, 3)
print('Input:', input)
output = torch.chunk(input, 3, dim=0)
print('Output:', output)
print('Output size:', len(output))
for i in range(len(output)):
    print('Output[{}]:'.format(i), output[i])