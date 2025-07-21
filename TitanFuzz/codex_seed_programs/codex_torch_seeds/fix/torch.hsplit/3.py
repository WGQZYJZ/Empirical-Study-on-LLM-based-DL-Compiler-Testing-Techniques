'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.hsplit\ntorch.hsplit(input, indices_or_sections)\n'
import torch
import torch
x = torch.arange(0, 16, dtype=torch.float32)
print('x =', x)
out1 = torch.hsplit(x, 4)
out2 = torch.hsplit(x, [3, 7])
print('out1 =', out1)
print('out2 =', out2)