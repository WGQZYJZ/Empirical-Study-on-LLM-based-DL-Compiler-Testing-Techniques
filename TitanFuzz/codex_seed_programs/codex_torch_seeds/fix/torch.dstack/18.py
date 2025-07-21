'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.dstack\ntorch.dstack(tensors, *, out=None)\n'
import torch
input_1 = torch.rand(2, 3, 4)
input_2 = torch.rand(2, 3, 4)
output = torch.dstack((input_1, input_2))
print('input_1:', input_1)
print('input_2:', input_2)
print('output:', output)