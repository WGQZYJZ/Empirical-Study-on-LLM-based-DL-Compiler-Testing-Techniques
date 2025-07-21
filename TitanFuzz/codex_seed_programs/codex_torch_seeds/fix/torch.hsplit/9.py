'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.hsplit\ntorch.hsplit(input, indices_or_sections)\n'
import torch
x = torch.arange(16, dtype=torch.float32).view(4, 4)
print('The original tensor: ', x)
y = torch.hsplit(x, 2)
print('The first sub-tensor: ', y[0])
print('The second sub-tensor: ', y[1])