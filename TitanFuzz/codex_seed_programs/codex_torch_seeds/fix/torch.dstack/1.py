'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.dstack\ntorch.dstack(tensors, *, out=None)\n'
import torch
input1 = torch.randn(3, 3)
input2 = torch.randn(3, 3)
output = torch.dstack([input1, input2])
print('Output: ', output)